from django.urls import path
from . import views
from .views import cart_view, add_to_cart, clear_cart, remove_from_cart  # Import your view

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cart/', cart_view, name='cart_page'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'), 
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('new/', views.new, name='new_arrivals'),
]