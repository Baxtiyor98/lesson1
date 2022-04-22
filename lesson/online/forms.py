from django import forms
from .models import *

class Yangiliklar(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        # fields = ['title','description','image']