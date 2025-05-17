from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import Product, Cart
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.
def basic(request):
    counter = Cart.objects.all().count()
    return render(request=request,template_name='basic.html', context = {'counter': counter})
def myproduct(request):
    items = Product.objects.all()
    counter = Cart.objects.all().count()
    return render(request=request,template_name='product.html', context = {'myproducts': items, 'counter': counter})
def mycart(request):
    cart = Cart.objects.all()
    return render(request=request,template_name='mycart.html',context = {'mycart': cart})
def cart_delete(request, id):
    ed = Cart.objects.get(id=id)
    ed.delete()
    return HttpResponseRedirect(reverse("mycart"))
#create view add cart.
def addtocart(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if (Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product Already in Cart."})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product added successfully."})
                    else:
                        return JsonResponse({'status': "Only" + str(product_check.quantity) + "quantity available."})
            else:
                return JsonResponse({'status': "No such product found."})
        else:
            return JsonResponse({'status': "Login to continuse"})
    return redirect('/')
    
# from .cart import Cart
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# def cart_add(request):
#     #Get the cart
#     cart = Cart(request)
#     #test foe POST
#     if request.POST.get('action') == 'post':
#         #get stuff
#         product_id = int(request.POST.get('product_id'))

#         #lookup product in DB
#         product = get_object_or_404(Product, id=product_id)

#         # Save to session
#         cart.add(product=product)

#         #Return Response
#         response = JsonResponse({'Product Name: ': product.name})
#         return render(request=request,template_name='mycart.hmtl')