from rest_framework import serializers
from .models import Product, ProductImage, Shop, ShopImage, Category



class ProductImageSerializer(serializers.ModelSerializer):
    product_image_url = serializers.FileField(source='images')

    class Meta:
        model = ProductImage
        fields = ('id', 'product_image_url')

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__' 



class ProductDetailSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(source='images', many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name')


class CategoryDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(many=True)
    
    class Meta:
        model = Category
        fields = '__all__'





class ShopImageSerializer(serializers.ModelSerializer):
    shop_image_url = serializers.FileField(source='images')

    class Meta:
        model = Shop
        fields = ('id', 'shop_image_url')


class ShopListSerializer(serializers.ModelSerializer):
    shop_image = ShopImageSerializer(source='images', many=True)

    class Meta:
        model = Shop
        fields = '__all__'



class ShopDetailSerializer(serializers.ModelSerializer):
    product_image = ShopImageSerializer(source='images', many=True)

    class Meta:
        model = Shop
        fields = "__all__"



