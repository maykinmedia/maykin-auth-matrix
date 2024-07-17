from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        "admin/auth_matrix/",
        include(("auth_matrix.admin_urls", "auth_matrix"), namespace="auth_matrix"),
    ),
    path("admin/", admin.site.urls),
]
