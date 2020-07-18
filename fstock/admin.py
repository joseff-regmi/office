from django.contrib import admin
from .models import Fstock

class FstockAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'fproduct_name', 'receipt_quantity', 'issued_quantity', 'balance_quantity')

    class Meta:
        model = Fstock



admin.site.register(Fstock, FstockAdmin)
