from django.urls import path
from .import views

urlpatterns=[
  path('',views.index,name='index'),
  path('menus',views.menus,name='menus'),
  path('plans',views.plans,name='plans'),
  path('login',views.login,name='login'), 
  path('cart',views.cart,name='cart'), 
  path('undercooking',views.undercooking,name='undercooking'),
]