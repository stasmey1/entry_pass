from django.forms import ModelForm
from .models import *


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['user', ]


fields = ['times_of_day', 'start', 'end', ]


class AddPassYearForm(ModelForm):
    class Meta:
        model = PassYear
        fields = fields


class AddPassOneTimeForm(ModelForm):
    class Meta:
        model = PassOneTime
        fields = fields


class UpdatePassYearForm(ModelForm):
    class Meta:
        model = PassYear
        fields = '__all__'


class UpdatePassOneTimeForm(ModelForm):
    class Meta:
        model = PassOneTime
        fields = '__all__'
