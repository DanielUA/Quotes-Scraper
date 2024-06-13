from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='home'),
    path('<int:page>/', views.main, name='root_paginate'),
    path('register/', views.register, name='register'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
]
