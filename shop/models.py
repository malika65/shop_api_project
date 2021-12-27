from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name = 'Название продукта')
    body = models.TextField(max_length=1500, verbose_name = 'Описание продукта')
    price = models.PositiveIntegerField()

    tags = models.ManyToManyField(Category,related_name = 'product', verbose_name = 'Категории')
  

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.product.name



class Shop(models.Model):
    name = models.CharField(max_length=200,verbose_name = 'Название магазина')
    body = models.TextField(max_length=1500, verbose_name = 'Описание магазина')
    address = models.CharField(max_length=100, verbose_name = 'Адрес магазина')
    telephone = models.CharField(max_length=50, verbose_name = 'Телефон магазина')
  

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class ShopImage(models.Model):
    shop = models.ForeignKey(Shop, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    class Meta:
        verbose_name = 'Изображение магазина'
        verbose_name_plural = 'Изображения магазинов'


    def __str__(self):
        return self.shop.name