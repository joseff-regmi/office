from django.db import models

# Create your models here.
class Rproduct(models.Model):
    rproduct_name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.rproduct_name


class Fproduct(models.Model):
    fproduct_name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.fproduct_name