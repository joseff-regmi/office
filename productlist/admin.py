from django.contrib import admin
from productlist.models import Rproduct, Fproduct

# Register your models here.
admin.site.register([Rproduct, Fproduct])