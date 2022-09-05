from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('login/', views.login, name='login'),
]