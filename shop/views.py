from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView

from .serializers import ProductListSerializer, ProductDetailSerializer

from .models import Product

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