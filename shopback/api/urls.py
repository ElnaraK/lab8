from django.urls import path
from api.views import products, product, categories, category, category_products

urlpatterns = [
    path('products/', products),
    path('products/<int:id>/', product),
    path('categories/', categories),
    path('categories/<int:id>/', category),
    path('categories/<int:id>/products/', category_products)
]