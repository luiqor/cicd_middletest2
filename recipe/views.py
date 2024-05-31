from django.shortcuts import render
from .models import Recipe


def main(request):
    random_recipies = Recipe.objects.all().order_by("?")[:10]

    return render(request, "main.html", context={"recipes": random_recipies})
