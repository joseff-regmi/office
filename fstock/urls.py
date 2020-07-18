from django.urls import path
from .views import products

app_name = 'fstock'

urlpatterns = [
    path('fstock', products, name='products'),




]