from django.contrib import admin
from django.urls import path
from . import views
from .views import view_cart, add_to_cart, remove_from_cart, home

urlpatterns = [
              path('',views.allproducts,name='allproducts'),
# urls.py







path('cart/', view_cart, name='view_cart'),
path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
path('login/', views.login_user, name='login'),
              path('logout/', views.logout_user, name='logout'),
              path('register/', views.register_user, name='register'),
              path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
              path('<slug:slug_c>/<slug_p>/' ,views.prod_det, name='product_catdetail'),


]


