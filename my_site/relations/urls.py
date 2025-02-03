from django.urls import path
from . import views

app_name = 'relatons'

urlpatterns = [
    path('', views.relations, name='relations'),
]
