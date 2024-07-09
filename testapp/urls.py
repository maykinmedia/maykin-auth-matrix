from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "admin/authorization/",
        include("auth_matrix.admin_urls"),
    ),
]
