from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from api.models import Product, Category
# Create your views here.

products_list = Product.objects.all()
products_list_json = [p.to_json() for p in products_list]

def products(request):
   return JsonResponse(products_list_json, safe=False)

def product(request, id):
   try:
      product_detail = Product.objects.get(id = id)
   except Product.DoesNotExist:
      return JsonResponse({'error': 'product does not exists'})
   return JsonResponse(product_detail.to_json())


def categories(request):
   category_list = Category.objects.all()
   category_list_json = [c.to_json() for c in category_list]
   return JsonResponse(category_list_json, safe=False)

def category(request, id):
   try:
      category_detail = Category.objects.get(id=id)
   except Category.DoesNotExist:
      return JsonResponse({'error': 'category does not exists'})
   return JsonResponse(category_detail.to_json())

def category_products(request, id):
   if id == 1:
      products = products_list_json[:5]
      return JsonResponse(products, safe = False)
   elif id == 2:
      products = products_list_json[5:10]
      return JsonResponse(products, safe=False)
   else:
      products = products_list_json[10:15]
      return JsonResponse(products, safe=False)