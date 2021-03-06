from django.urls import path

from .views import index, ProductListView, ProductDetailView, ShopListView, ShopDetailView, CategoryListView, CategoryDetailView

app_name = 'shop'

urlpatterns = [
    path('index/', index),
    path('categories/',CategoryListView.as_view()),
    path('categories/<int:category_id>/',CategoryDetailView.as_view()),
    path('products/',ProductListView.as_view()),
    path('products/<int:product_id>/',ProductDetailView.as_view()),
    path('shops/',ShopListView.as_view()),
    path('shops/<int:shop_id>/',ShopDetailView.as_view()),

]