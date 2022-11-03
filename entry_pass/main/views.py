from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from .mixins import *
from .utils import *


class HomePage(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'main\index.html'


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

    def get_context_data(self, **kwargs):
        context = super(DetailCar, self).get_context_data(**kwargs)
        context['year_passes'] = PassYear.objects.filter(car=self.get_object().pk)
        context['one_time_passes'] = PassOneTime.objects.filter(car=self.get_object().pk)
        return context


class DeleteCar(DeleteView):
    model = Car
    template_name = 'main\\delete_car.html'
    success_url = '/'


def add_pass_year(request, pk):
    times_of_day = 'Годовой пропуск'
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = AddPassYearForm(request.POST)
        if form.is_valid():
            new_pass_year = form.save(commit=False)
            new_pass_year.car = car
            new_pass_year.save()
            return redirect('index')
    form = AddPassYearForm(initial={
        'start': datetime.now().date(),
        'end': datetime.now().date() + timedelta(days=364),
    })
    template = 'main\pass_form.html'
    return render(request, template, locals())


class UpdatePassYear(UpdateView):
    model = PassYear
    form_class = UpdatePassYearForm
    template_name = 'main\pass_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['times_of_day'] = 'Годовой пропуск'
        return context


class DeletePassYear(DeleteView):
    model = PassYear
    template_name = 'main\\delete_pass.html'
    success_url = '/'


class DeletePassOneTime(DeleteView):
    model = PassOneTime
    template_name = 'main\\delete_pass.html'
    success_url = '/'


def add_pass_one_time(request, pk):
    times_of_day = 'Разовый пропуск'
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = AddPassOneTimeForm(request.POST)
        if form.is_valid():
            new_pass = form.save(commit=False)
            new_pass.car = car
            new_pass.save()
            return redirect('index')
    form = AddPassOneTimeForm(initial={
        'start': datetime.now().date(),
        'end': datetime.now().date() + timedelta(days=9),
    })
    template = 'main\pass_form.html'
    return render(request, template, locals())


class UpdatePassOneTime(UpdateView):
    model = PassOneTime
    form_class = UpdatePassOneTimeForm
    template_name = 'main\pass_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['times_of_day'] = 'Разовый пропуск'
        return context