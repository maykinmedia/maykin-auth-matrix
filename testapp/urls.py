from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/auth_matrix/", include(("auth_matrix.admin_urls"))),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
