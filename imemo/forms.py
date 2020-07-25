from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class meta:
        model = Memo