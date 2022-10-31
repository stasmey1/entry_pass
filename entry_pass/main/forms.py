from django.forms import ModelForm
from .models import *

from urllib import request


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class PassForm(ModelForm):
    class Meta:
        model = Pass
        fields = '__all__'
