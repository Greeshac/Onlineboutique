from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Category, Product, Cart


def allproducts(request, slug_c=None):
    page_c=None
    products=None
    if slug_c!=None:
        page_c=get_object_or_404(Category, slug=slug_c)
        products=Product.objects.all().filter(category=page_c,available=True)

    else:
        products=Product.objects.all().filter(available=True)

    return render(request,'home.html',{'category':page_c ,'products':products})

def prod_det(request, slug_c, slug_p):
    try:
        product=Product.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product':product})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('allproducts')
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})


def logout_user(request):
    logout(request)
    return redirect('login')



def home(request):
    return render(request,'home.html', {'userName' : request.user.username})

from .forms import UserRegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')


