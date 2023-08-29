from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.myfirst, name='products'),
    path('all/', views.all, name='all'),
    path('accessories/', views.accessories, name='accessories'),
    path('boy/', views.boy, name='boy'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
]