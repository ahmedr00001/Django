from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.forms, name='forms'),
    path('forms2', views.forms2, name='forms2'),
    path('forms3', views.forms3, name='forms3'),
]
