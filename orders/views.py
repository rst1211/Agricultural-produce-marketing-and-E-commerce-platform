from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cart.cart import Cart
from datetime import date

def od(request):
    username=request.session['username']
    return render(request,"checkout.html",{'username':username})

def order_create(request):
    username = request.session['username']
    cart = Cart(request)
    if request.method == 'POST':
        for item in cart:
            x=item['product']
            f = {'name': username, 'phone': request.POST['phone'],'product':x.prodname, 'qty':item['quantity'],'day':date.today(),
                 'pin': request.POST['pincode'], 'address': request.POST['address']}

            form = OrderForm(f)
            if form.is_valid():
                form.save()

            cart.clear()
            return render(request, 'customer.html', {'username': username})
    else:
        form = OrderForm()
        return render(request, 'customer.html', {'username': username})

def myorder(request):
    username=request.session['username']
    orders=Order.objects.filter(name=username)
    return render(request,'myorders.html',{'orders':orders})

