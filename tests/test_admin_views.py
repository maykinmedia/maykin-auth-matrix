from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest

from auth_matrix.admin_views import AuthorizationMatrixView

User = get_user_model()


@pytest.fixture
def url():
    return reverse("auth_matrix:authorization_matrix")


@pytest.fixture
def view():
    return AuthorizationMatrixView.as_view()


@pytest.mark.django_db
def test_view_requires_admin_permission(client, url):
    # Create a non-admin user and log in
    user = User.objects.create_user(
        username="test_user", password="test_pass", is_staff=False, is_superuser=False
    )
    client.force_login(user)

    response = client.get(url)

    # Expecting redirect to login since PermissionDenied should lead to a
    # redirect to login page when using client
    assert response.status_code == 302


def test_view_returns_200_for_admin_user(admin_client, url):
    response = admin_client.get(url)

    assert response.status_code == 200


def test_view_uses_correct_template(admin_client, url):
    response = admin_client.get(url)

    assert "admin/auth_matrix/authorization_matrix.html" in [
        t.name for t in response.templates
    ]


def test_view_context_contains_groups(admin_client, url):
    response = admin_client.get(url)

    assert "groups" in response.context


def test_view_context_contains_user_group_matrix(admin_client, url):
    response = admin_client.get(url)

    assert "user_group_matrix" in response.context
    assert isinstance(response.context["user_group_matrix"], list)


def test_view_context_contains_group_permission_matrix(admin_client, url):
    response = admin_client.get(url)

    assert "group_permission_matrix" in response.context
    assert isinstance(response.context["group_permission_matrix"], list)
