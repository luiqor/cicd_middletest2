from django.contrib import admin
from django.urls import path
from recipe.views import main, category_detail


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main, name="main"),
    path("category/<str:category_name>", category_detail, name="category_detail"),
]
