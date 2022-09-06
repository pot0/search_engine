from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# from .models import Order

# Register your models here.

class UserAdmin(admin.ModelAdmin): #model, admin관련 클래스 상속
    list_display = ('username', 'password') #admin페이지에서 해당 모델을 어떻게 리스트화해서 보여줄 것인지 지정

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product')

# admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin) #모델과 admin클래스 지정해서 등록