from modulefinder import ModuleFinder
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='상품명', max_length=256)
    price = models.IntegerField(verbose_name='상품가격')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modifiedDate = models.DateTimeField(auto_now_add=True, verbose_name='수정날짜')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'product'
        verbose_name = '상품'
        verbose_name_plural = '상품'