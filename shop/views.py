from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView

from .serializers import (
    CategoryListSerializer,
    ProductListSerializer, 
    ProductDetailSerializer, 
    ShopListSerializer, 
    ShopDetailSerializer,
    CategoryDetailSerializer
)

from .models import Product, Shop, Category

def index(request):
    return HttpResponse("Hello world")  


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDetailView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'category_id'
   


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'product_id'


class ShopListView(ListAPIView):
    serializer_class = ShopListSerializer
    queryset = Shop.objects.all()


class ShopDetailView(RetrieveAPIView):
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()
    lookup_field = 'pk' # id
    lookup_url_kwarg = 'shop_id'