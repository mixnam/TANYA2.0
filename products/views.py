from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())

def boots(request):
	return render(request, 'products/boots.html', locals())

def snikers(request):
	return render(request, 'products/snikers.html', locals())

def t_shirt(request):
    
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)

    return render(request, 'products/t-shirt.html', locals())

def jackets(request):
	return render(request, 'products/jackets.html', locals())

def pants(request):
	return render(request, 'products/pants.html', locals())