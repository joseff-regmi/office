from django.urls import path
from .views import products, entry_fproducts

app_name = 'fstock'

urlpatterns = [
    path('fstock', products, name='products'),
    path('entry_fproducts', entry_fproducts, name='fproducts')




]