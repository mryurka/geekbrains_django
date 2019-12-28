from django.urls import path
from adminapp.views import ProductListView
from adminapp.views import ProductDetailView
from adminapp.views import ProductCreateView
from adminapp.views import ProductUpdateView
from adminapp.views import ProductDeleteView
from adminapp.views import UserListView
from adminapp.views import UserUpdateView
from adminapp.views import UserCreateView
from adminapp.views import UserDeleteView
from adminapp.views import CategoryCreateView
from adminapp.views import CategoryUpdateView
from adminapp.views import CategoryDeleteView


app_name = 'adminapp'

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/read/', ProductListView.as_view(), name='product'),
    path('product/read/cat/<cat_pk>', ProductListView.as_view(), name='category'),
    path('product/read/<pk>', ProductDetailView.as_view(), name='detail'),
    path('product/update/<pk>', ProductUpdateView.as_view(), name='update'),
    path('product/del/<pk>', ProductDeleteView.as_view(), name='delete'),
    # ------------------------------------------------------------------
    path('product/user_create/', UserCreateView.as_view(), name='user_create'),
    path('user/read/', UserListView.as_view(), name='user'),
    path('product/user_update/<pk>', UserUpdateView.as_view(), name='user_update'),
    path('product/user_delete/<pk>', UserDeleteView.as_view(), name='user_delete'),
    # ------------------------------------------------------------------
    path('product/cat_create/', CategoryCreateView.as_view(), name='cat_create'),
    path('product/cat_update/<pk>', CategoryUpdateView.as_view(), name='cat_update'),
    path('product/cat_delete/<pk>', CategoryDeleteView.as_view(), name='cat_delete'),
]

