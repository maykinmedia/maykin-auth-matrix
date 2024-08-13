from auth_matrix.admin_views import get_auth_matrix_permission_label


def auth_matrix_permission(request):
    return {
        "can_view_auth_matrix": (
            request.user.has_perm(get_auth_matrix_permission_label())
            if request.user.is_authenticated
            else False
        )
    }
