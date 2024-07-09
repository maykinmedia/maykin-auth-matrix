from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "admin/authorization/",
        include("auth_matrix.admin_urls"),
    ),
    path("admin/", admin.site.urls),
]
