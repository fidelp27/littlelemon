from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_restaurant'),
    path('menu/', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
]
