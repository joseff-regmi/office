from django.db import models
from productlist.models import Rproduct, Fproduct

# Create your models here.
class Purchese(models.Model):
    rproduct_id = models.IntegerField(primary_key=True)
    pragyapan_no = models.CharField(max_length=100, null=False, blank=False)
    rproduct_name = models.ForeignKey(Rproduct, on_delete=models.CASCADE)
    rproduct_quantity = models.IntegerField()


    def __str__(self):
        return self.rproduct_name
    
    