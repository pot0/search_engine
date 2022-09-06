from itertools import product
from tabnanny import verbose
from django.db import models

# Create your models here.
class Order(models.Model):
    # user = models.ForeignKey('user.User', verbose_name='사용자', on_delete=models.CASCADE)
    # order = models.ForeignKey('product.Product', verbose_name='상품', on_delete=models.CASCADE)
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    modifiedDate = models.DateTimeField(auto_now_add=True, verbose_name='수정날짜')

def __str__(self):
    return str(self.user) + '' + str(self.product)

class Meta:
    db_table = 'order'
    verbose_name = '주문'
    verbose_name_plural = '주문'