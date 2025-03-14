from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})
                  

def new(request):
    latest_products = Product.objects.order_by('-id')[:4]  # Fetch last 4 added products
    return render(request, 'new_arrivals.html', {'latest_products': latest_products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('products:cart')

@login_required
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)  # Use cart__user instead of user
        total_price = sum(item.total_price() for item in cart_items)
    except Cart.DoesNotExist:
        cart_items = []
        total_price = 0

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('products:cart')

@login_required
def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.cartitem_set.all().delete()
    return redirect('products:cart_page')

@login_required
def clear_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()  # Correct way to clear cart items
    except Cart.DoesNotExist:
        pass  # If cart doesn't exist, do nothing

    return redirect('products:cart')  # Fix redirect

def home(request):
    new_arrivals = Product.objects.order_by('-id')[:4]  # Last 4 added products
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'home.html', {'new_arrivals': new_arrivals, 'categories': categories})