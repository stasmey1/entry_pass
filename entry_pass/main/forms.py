from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *


class ValidationMixin:

    def clean(self):
        super().clean()
        if self.cleaned_data['start'] > self.cleaned_data['end']:
            raise ValidationError('Начало срока пропуска не может быть позже чем его конец')


fields = ['start', 'end', ]


class PassDayYearForm(ValidationMixin, ModelForm):
    class Meta:
        model = PassDayYear
        fields = fields


class PassNightYearForm(ValidationMixin, ModelForm):
    class Meta:
        model = PassNightYear
        fields = fields


class PassOneTimeForm(ValidationMixin, ModelForm):
    class Meta:
        model = PassOneTime
        fields = fields


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['user',
                   'can_update_pass_year_day',
                   'date_of_application_pass_year_day',
                   'date_new_pass_year_day',
                   'can_update_pass_year_night',
                   'date_of_application_pass_year_night',
                   'date_new_pass_year_night',
                   'can_update_pass_one_time',
                   'date_of_application_pass_one_time',
                   'date_new_pass_one_time']


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'