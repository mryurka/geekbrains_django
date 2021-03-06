"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from django.urls import re_path
from mainapp.views import main
from mainapp.views import products
from mainapp.views import contacts

app_name = 'mainapp'

urlpatterns = [
    path(r'', main, name='main'),
    # re_path(r'^products/(?P<product_category>\w+)/$', products, name='products'),
    path(r'products/<int:category_pk>/', products, name='products'),
    path(r'contacts/', contacts, name='contacts'),
]
