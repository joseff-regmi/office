from django.shortcuts import render, redirect
from .models import Fstock
from .forms import FstockForm

# Create your views here.

def products(request):
    products = Fstock.objects.all()
    context = {
        'products' : products
    }

    return render(request, template_name='fstock.html', context= context)


def entry_fproducts(request):
    if request.method == 'POST':
        form = FstockForm(request.POST or none)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form = FstockForm()
    return render(request, "entry_fproducts.html", {'form': form})

        