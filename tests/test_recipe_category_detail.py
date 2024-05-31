from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_category_detail_view_status(client, categories, recipes):
    category = categories[0]
    url = reverse("category_detail", args=[category.name])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("category_index", [0, 1, 2])
def test_category_detail_view(client, categories, recipes, category_index):
    """Test that the category detail view returns the correct recipes."""
    category = categories[category_index]
    url = reverse("category_detail", args=[category.name])
    response = client.get(url)

    expected_recipes = category.categories.all()
    assert list(response.context["recipes"]) == list(expected_recipes)
