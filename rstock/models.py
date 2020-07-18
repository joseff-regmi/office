from django.db import models

# Create your models here.
from django.db import models


class Rproduct(models.Model):
    name_of_article = models.CharField(max_length=100, null=True, blank=False)
    date = models.DateTimeField
    particulars = models.CharField(max_length=100, null=True, blank=True)
    receipt_quantity = models.IntegerField(null=True, blank=True)
    issued_quantity = models.IntegerField(null=True, blank=True)
    balance_quantity = models.IntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = 'rproduct'


    def __str__(self):
        return self.name_of_article