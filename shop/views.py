from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView

from .serializers import ProductListSerializer, ProductDetailSerializer, ShopListSerializer, ShopDetailSerializer

from .models import Product, Shop

def index(request):
    return HttpResponse("Hello world")  

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