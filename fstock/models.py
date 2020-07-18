from django.db import models
from productlist.models import Fproduct


class Fstock(models.Model):
    fproduct_name = models.ForeignKey(Fproduct, on_delete=models.CASCADE)
    date = models.DateTimeField
    particulars = models.CharField(max_length=100, null=True, blank=True)
    receipt_quantity = models.IntegerField(null=True, blank=True)
    issued_quantity = models.IntegerField(null=True, blank=True)
    balance_quantity = models.IntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = 'fproduct'


    def __str__(self):
        return self.fproduct_name