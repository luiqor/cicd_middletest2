import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_main_view_status_code(client):
    response = client.get(reverse("main"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_main_10items_max(client, recipes):
    """Test that the main view returns a maximum of 10 recipes."""
    response = client.get("/")

    assert len(response.context["recipes"]) <= 10
