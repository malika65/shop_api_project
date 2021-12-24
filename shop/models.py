from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name = 'Название продукта')
    body = models.TextField(max_length=1500, verbose_name = 'Описание продукта')
    price = models.PositiveIntegerField()
  

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