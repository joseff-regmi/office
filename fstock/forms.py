from django.contrib.auth.forms import forms
from .models import Fstock

class FstockForm(forms.ModelForm):

        class meta:
                model = Fstock
                include = ('__all__')