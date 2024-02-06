from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products":cart_products, 'quantities':quantities})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get product id
        product_id = int(request.POST.get('product_id'))
        # Get product quantity
        product_qty = int(request.POST.get('product_qty'))
        # Check if product_qty is not None
        if product_qty is not None:
            try:
                # Attempt to convert product_qty to int
                product_qty = int(product_qty)
                
                # Lookup product in DB
                product = get_object_or_404(Product, id=product_id)
                # Save to session
                cart.add(product=product, quantity=product_qty)
                # Get Cart Quantity
                cart_quantity = cart.__len__()
                
                # Return response
                # response = JsonResponse({'Product Name': product.name})
                response = JsonResponse({'qty': cart_quantity})
                return response
            except ValueError:
                # Handle the case where product_qty is not a valid integer
                pass
        
        # Handle the case where product_qty is None or not a valid integer
        return JsonResponse({'error': 'Invalid product quantity'})
    


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        # Call delete function in cart.py
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get product id
        product_id = int(request.POST.get('product_id'))
        # Get product quantity
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        respponse = JsonResponse({'qty':product_qty})
        return respponse
        # return redirect('cart_summary')
        