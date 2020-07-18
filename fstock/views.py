from django.shortcuts import render
from .models import Fstock

# Create your views here.

def products(request):
    products = Fstock.objects.all()
    context = {
        'products' : products
    }

    return render(request, template_name='fstock.html', context= context)