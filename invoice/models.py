from django.db import models
from fstock.models import Fproduct

# Create your models here.

class Bill(models.Model):
    bill_no = models.IntegerField(null=False, blank=False)
    fproduct_name = models.ForeignKey(Fproduct, on_delete=models.CASCADE)
    rate = models.IntegerField(null=False, blank=False)
