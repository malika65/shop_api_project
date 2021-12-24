from django.urls import path

from .views import index, ProductListView, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('index/', index),
    path('products/',ProductListView.as_view()),
    path('products/<int:product_id>/',ProductDetailView.as_view()),

]