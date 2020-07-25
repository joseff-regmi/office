from django.db import models
import datetime 
from productlist.models import Fproduct, Rproduct


class Memo(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField
    fproducts = models.ForeignKey(Fproduct, blank=True, null=True,  on_delete=models.CASCADE)
    rproducts = models.ForeignKey(Rproduct, blank=True, null=True,  on_delete=models.CASCADE)


    def __int__(self):
        return self.id