from .models import *
from .forms import *


class CarMixin:
    model = Car
    template_name = 'main\car_form.html'
    form_class = CarForm




