from django.contrib import admin
from django.urls import path

from .admin_views import AuthorizationMatrixView

urlpatterns = [
    path(
        "matrix",
        admin.site.admin_view(AuthorizationMatrixView.as_view()),
        name="authorization_matrix",
    ),
]
