from django.urls import path
import authapp.views as authapp_view

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp_view.login, name='login'),
    path('logout/', authapp_view.logout, name='logout'),
    path('register/', authapp_view.register, name='register'),
    path('edit/', authapp_view.edit, name='edit'),
    path('verify/<str:email>/<str:activation_key>/', authapp_view.verify, name='verify'),
]

