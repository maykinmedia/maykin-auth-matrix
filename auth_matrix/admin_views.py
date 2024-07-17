from django import views
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class UserIsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


def get_auth_matrix_permission():
    if User._meta.app_label == "auth":
        return "auth.view_user"
    return "accounts.view_user"


class AuthorizationMatrixView(
    UserIsStaffMixin, PermissionRequiredMixin, views.generic.base.TemplateView
):
    permission_required = get_auth_matrix_permission()
    template_name = "admin/auth_matrix/authorization_matrix.html"

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
