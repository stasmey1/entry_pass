from django.forms import ModelForm
from .models import *

fields = ['times_of_day', 'start', 'end', ]


class AddPassYearForm(ModelForm):
    class Meta:
        model = PassYear
        fields = fields


class AddPassOneTimeForm(ModelForm):
    class Meta:
        model = PassOneTime
        fields = fields


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['user', ]


class UpdatePassYearForm(ModelForm):
    class Meta:
        model = PassYear
        fields = '__all__'


class UpdatePassOneTimeForm(ModelForm):
    class Meta:
        model = PassOneTime
        fields = '__all__'


class AddOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'