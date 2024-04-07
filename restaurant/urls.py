from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('home/', views.home, name='home_restaurant'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('logoff/', views.logoff, name='logoff'),
    path('menu/', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('api-token-auth/', obtain_auth_token),
]
