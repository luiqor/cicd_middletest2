import pytest
from recipe.models import Category, Recipe


@pytest.fixture
def categories(db):
    """Create multiple category instances for testing."""
    category1 = Category.objects.create(name="category1")
    category2 = Category.objects.create(name="category2")
    category3 = Category.objects.create(name="category3")
    return [category1, category2, category3]


@pytest.fixture
def recipes(categories, db):
    """Create multiple recipe instances for testing."""
    recipe1 = Recipe.objects.create(
        title="Recipe 1",
        description="Description for Recipe 1",
        instructions="Instructions for Recipe 1",
        ingredients="Ingredients for Recipe 1",
        category=categories[0],
    )
    recipe2 = Recipe.objects.create(
        title="Recipe 2",
        description="Description for Recipe 2",
        instructions="Instructions for Recipe 2",
        ingredients="Ingredients for Recipe 2",
        category=categories[1],
    )
    recipe3 = Recipe.objects.create(
        title="Recipe 3",
        description="Description for Recipe 3",
        instructions="Instructions for Recipe 3",
        ingredients="Ingredients for Recipe 3",
        category=categories[2],
    )
    return [recipe1, recipe2, recipe3]
