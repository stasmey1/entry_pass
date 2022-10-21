from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from .mixins import *


def index(request):
    cars = Car.objects.all()
    template = 'main\index.html'
    return render(request, template, locals())


class AddCar(CarMixin, CreateView):
    pass


class UpdateCar(CarMixin, UpdateView):
    pass


class DetailCar(DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'main\car.html'


class DeleteCar(DeleteView):
    model = Car
    template_name = 'main\\delete_car.html'
    success_url = '/'


class AddPassYear(PassYearMixin, CreateView):
    pass


class UpdatePassYear(PassYearMixin, UpdateView):
    pass


class DetailPassYear(DetailView):
    model = PassYear
    context_object_name = 'pass'
    template_name = 'main\pass.html'


class DeletePassYear(DeleteView):
    model = PassYear
    template_name = 'main\\delete_pass.html'
    success_url = '/'


class AddPassTenDays(PassTenDaysMixin, CreateView):
    pass


class UpdatePassTenDays(PassYearMixin, UpdateView):
    pass


class DetailPassTenDays(DetailView):
    model = PassTenDays
    context_object_name = 'pass'
    template_name = 'main\pass_year.html'


class DeletePassTenDays(DeleteView):
    model = PassTenDays
    template_name = 'main\\delete_pass.html'
    success_url = '/'