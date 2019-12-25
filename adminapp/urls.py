from django.urls import path
from adminapp.views import ProductListView
from adminapp.views import ProductDetailView
from adminapp.views import ProductCreateView
from adminapp.views import ProductUpdateView
from adminapp.views import ProductDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/read/', ProductListView.as_view(), name='product'),
    path('product/read/cat/<cat_pk>', ProductListView.as_view(), name='category'),
    path('product/read/<pk>', ProductDetailView.as_view(), name='detail'),
    path('product/update/<pk>', ProductUpdateView.as_view(), name='update'),
    path('product/del/<pk>', ProductDeleteView.as_view(), name='delete'),

]

