from .models import *
from .forms import *


class CarMixin:
    model = Car
    template_name = 'main\car_form.html'
    form_class = CarForm


class PassMixin:
    model = Pass
    template_name = 'main\\pass_form.html'
    form_class = PassForm



