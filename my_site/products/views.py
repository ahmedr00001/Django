from django.shortcuts import render
from .models import Product

# Create your views here.

def products (request) :
    pro = Product.objects.all()
    pro_count =Product.objects.all().count()  #to display count
    # pro_orderd =Product.objects.all().order_by('name')  #order by name
    # pro_orderd =Product.objects.all().filter(price=10)  #only retuen this
    # pro_orderd =Product.objects.all().filter(price__range(100,800))  #range of 100 :800
    # pro_orderd =Product.objects.all().filter(name__contians='a')  #any item contian a in name
    # pro_orderd =Product.objects.all().exclude(price=10)  #all exclude this


    return render(request, 'products/products.html', {'pro':pro , 'pro_count':pro_count} )
    #you can use Product.object.ger(name = 'reno 4') to return one object
def product (request) :
    return render(request ,'products/product.html'  )