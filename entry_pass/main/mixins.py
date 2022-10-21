from .models import *
from .forms import *


class CarMixin:
    model = Car
    template_name = 'main\car_form.html'
    form_class = CarForm


class PassYearMixin:
    model = PassYear
    template_name = 'main\\pass_form.html'
    form_class = PassYearForm


class PassTenDaysMixin:
    model = PassTenDays
    template_name = 'main\\pass_form.html'
    form_class = PassTenDays


