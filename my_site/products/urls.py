from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('product/', views.product, name='product'),
    path('', views.products, name='products'),
]
