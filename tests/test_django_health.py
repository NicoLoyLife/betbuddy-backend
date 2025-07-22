import pytest
from django.test import Client


@pytest.mark.django_db
def test_admin_login_page_accessible():
    client = Client()
    response = client.get("/admin/")
    assert response.status_code == 200
