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
        exclude = ['user', 'can_update_pass_year_day', 'date_of_application_pass_year_day', 'date_new_pass_year_day',
                   'can_update_pass_year_night', 'date_of_application_pass_year_night', 'date_new_pass_year_night',
                   'can_update_pass_one_time', 'date_of_application_pass_one_time', 'date_new_pass_one_time']


class UpdatePassYearForm(ModelForm):
    class Meta:
        model = PassYear
        fields = '__all__'


class UpdatePassOneTimeForm(ModelForm):
    class Meta:
        model = PassOneTime
        fields = '__all__'


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
