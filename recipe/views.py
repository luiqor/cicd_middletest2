from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category


def main(request):
    random_recipies = Recipe.objects.all().order_by("?")[:10]

    return render(request, "main.html", context={"recipes": random_recipies})


def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    recipes = category.categories.all()
    context = {
        "category": category,
        "recipes": recipes,
    }
    return render(request, "category_detail.html", context)
