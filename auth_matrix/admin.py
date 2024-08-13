from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import OuterRef, Subquery, Value

from import_export import fields, resources
from import_export.admin import ExportMixin

# USERS

User = get_user_model()

username_attribute = getattr(User, "USERNAME_FIELD", "username")
email_attribute = getattr(User, "EMAIL_FIELD", "email")


class UserWithGroupsResource(resources.ModelResource):
    username = fields.Field(attribute=username_attribute, column_name="Username")
    email = fields.Field(attribute=email_attribute, column_name="E-mail")
    last_login = fields.Field(attribute="last_login", column_name="Laatst gewijzigd")
    is_active = fields.Field(attribute="is_active", column_name="Actief")
    is_staff = fields.Field(attribute="is_staff", column_name="Admin toegang")
    is_superuser = fields.Field(
        attribute="is_superuser", column_name="Admin supergebruiker"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
        )
        export_order = fields

    def after_export(self, queryset, data, *args, **kwargs):
        group_names_subquery = (
            Group.objects.filter(user=OuterRef("pk"))
            .values("user")
            .annotate(group_names=ArrayAgg("name"), default=Value([]))
            .values("group_names")
        )
        queryset = queryset.annotate(group_names=Subquery(group_names_subquery))
        for group_name in Group.objects.values_list("name", flat=True).order_by("name"):
            column = [group_name in (user.group_names or []) for user in queryset]
            data.append_col(column, header=group_name)
        return data


class UserExportMixin(ExportMixin):
    resource_classes = (UserWithGroupsResource,)
    change_list_template = "admin/auth/user/change_list.html"


# GROUPS


class GroupPermissionResource(resources.ModelResource):
    name = fields.Field(attribute="name", column_name="Groep")

    class Meta:
        model = Group
        fields = ("name",)
        export_order = fields

    def after_export(self, queryset, data, *args, **kwargs):
        # Get all permissions with their content type and codename
        # Permissions names aint unique, so we need to include the content type
        # and the model to make them unique
        permissions = Permission.objects.prefetch_related("content_type").values(
            "content_type__app_label", "content_type__model", "codename"
        )

        # Create a list of formatted permission names
        permission_names = [
            f"{perm['content_type__app_label']}:"
            f"{perm['content_type__model']}:{perm['codename']}"
            for perm in permissions
        ]

        # Iterate over the formatted permission names
        for permission_name in permission_names:
            app_label, model, codename = permission_name.split(":")
            data.append_col(
                [
                    group.permissions.filter(
                        content_type__app_label=app_label,
                        content_type__model=model,
                        codename=codename,
                    ).exists()
                    for group in queryset
                ],
                header=permission_name,
            )
        dataset = data.transpose()
        # Rename the first column to "Groep"
        dataset.headers[0] = "Groep"
        return dataset


class GroupExportMixin(ExportMixin):
    resource_classes = (GroupPermissionResource,)
    change_list_template = "admin/auth/group/change_list.html"

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "permissions":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs["queryset"] = qs.select_related("content_type")
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)
