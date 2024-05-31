from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category


def main(request):
    """View function for the main page.
    This view returns a list of max of 10 random recipes
    to display on the main page.
    Args:
        request: The request object.
    Returns:
        recipes: A list of 10 random recipes.
    """
    random_recipies = Recipe.objects.all().order_by("?")[:10]

    return render(request, "main.html", context={"recipes": random_recipies})


def category_detail(request, category_name):
    """This view returns a list of recipes that belong to the category
    by accessing 'category/category_name'
    Args:
        request: The request object.
        category_name: The name of the category.
    Returns:
        category: The category object.
        recipes: A list of recipes that belong to the category.
    """
    category = get_object_or_404(Category, name=category_name)
    recipes = category.categories.all()
    context = {
        "category": category,
        "recipes": recipes,
    }
    return render(request, "category_detail.html", context)
