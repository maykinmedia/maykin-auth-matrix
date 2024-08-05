from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, Permission
from django.views.generic import TemplateView

User = get_user_model()


class UserIsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


def get_auth_matrix_permission_label():
    opts = User._meta
    return f"{opts.app_label}.view_{opts.model_name}"


class CanViewAuthorizationMatrixMixin(UserIsStaffMixin, PermissionRequiredMixin):

    def get_permission_required(self):
        permission_required = get_auth_matrix_permission_label()
        return (permission_required,)


class AuthorizationMatrixView(
    CanViewAuthorizationMatrixMixin,
    TemplateView,
):
    template_name = "auth_matrix/admin/authorization_matrix.html"

    def get(self, request):
        groups = Group.objects.prefetch_related("permissions").order_by("name")
        users = User.objects.prefetch_related("groups")
        permissions = Permission.objects.all().order_by(
            "content_type__app_label", "name"
        )

        user_group_matrix = [
            {"user": user, "groups": [group in user.groups.all() for group in groups]}
            for user in users
        ]

        group_permission_matrix = [
            {
                "permission": permission,
                "groups": [permission in group.permissions.all() for group in groups],
            }
            for permission in permissions
        ]

        context = {
            "groups": groups,
            "user_group_matrix": user_group_matrix,
            "group_permission_matrix": group_permission_matrix,
        }

        return self.render_to_response(context)
