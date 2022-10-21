from django.forms import ModelForm
from .models import *


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class PassYearForm(ModelForm):
    class Meta:
        model = PassYear
        fields = '__all__'


class PassTenDays(ModelForm):
    class Meta:
        model = PassTenDays
        fields = '__all__'
