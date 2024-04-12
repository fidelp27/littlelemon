from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('home/', views.home, name='home_restaurant'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logoff/', views.logoff, name='logoff'),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:category_id>/', views.menu, name='menu_category'),    
]
