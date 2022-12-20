from django.forms import ModelForm
from .models import *

fields = ['start', 'end', ]


class PassDayYearForm(ModelForm):
    class Meta:
        model = PassDayYear
        fields = fields


class PassNightYearForm(ModelForm):
    class Meta:
        model = PassNightYear
        fields = fields


class PassOneTimeForm(ModelForm):
    class Meta:
        model = PassOneTime
        fields = fields


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['user', 'can_update_pass_year_day', 'date_of_application_pass_year_day', 'date_new_pass_year_day',
                   'can_update_pass_year_night', 'date_of_application_pass_year_night', 'date_new_pass_year_night',
                   'can_update_pass_one_time', 'date_of_application_pass_one_time', 'date_new_pass_one_time']


# class UpdatePassDayYearForm(ModelForm):
#     class Meta:
#         model = PassDayYear
#         fields = '__all__'
#
#
# class UpdatePassNightYearForm(ModelForm):
#     class Meta:
#         model = PassNightYear
#         fields = '__all__'


# class UpdatePassOneTimeForm(ModelForm):
#     class Meta:
#         model = PassOneTime
#         fields = '__all__'


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
