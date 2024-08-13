from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.contrib.auth.models import Group, User

from auth_matrix.admin import GroupExportMixin, UserExportMixin

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserExportMixin, _UserAdmin):
    pass


admin.site.unregister(Group)


@admin.register(Group)
class CustomGroupAdmin(GroupExportMixin, admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = ("permissions",)
    pass
