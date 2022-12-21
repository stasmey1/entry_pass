from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
from .utils import *
from .constants import *


def index(request):
    cars = Car.objects.all()
    find_actual_passes(cars)
    template = 'main\index.html'
    return render(request, template, locals())


def update_passes_status(request):
    cars = Car.objects.all()
    for car in cars:
        car.update_passes_status()
    return redirect('index')


class AddCar(CreateView):
    model = Car
    template_name = 'main\car\car_form.html'
    form_class = CarForm


class UpdateCar(UpdateView):
    model = Car
    template_name = 'main\car\car_form.html'
    form_class = CarForm


class DetailCar(DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'main\car\car.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCar, self).get_context_data(**kwargs)
        context['year_pass_day'] = PassDayYear.objects.filter(car=self.get_object().pk)
        context['year_pass_night'] = PassNightYear.objects.filter(car=self.get_object().pk)
        context['one_time_passes'] = PassOneTime.objects.filter(car=self.get_object().pk).order_by('-start')
        return context


class DeleteCar(DeleteView):
    model = Car
    template_name = 'main\car\\delete_car.html'
    success_url = '/'


def add_pass(request, pk_car, form_pass_class):
    form_pass_class = forms_dict.get(form_pass_class)
    car = Car.objects.get(pk=pk_car)
    if request.method == "POST":
        form = form_pass_class(request.POST)
        if form.is_valid():
            new_pass_year = form.save(commit=False)
            new_pass_year.car = car
            new_pass_year.save()
            return redirect('index')
    else:
        if not form_pass_class.__name__ == 'PassOneTimeForm':
            form = form_pass_class(initial={
                'start': datetime.now().date(),
                'end': datetime.now().date() + timedelta(days=364),
            })
        else:
            form = form_pass_class(initial={
                'start': datetime.now().date(),
                'end': datetime.now().date() + timedelta(days=10)
            })

    template = 'main\pass\pass_form.html'
    return render(request, template, locals())


def update_pass(request, pk, pass_class, form_pass_class):
    pass_class = passes_class_dict.get(pass_class)
    form_pass_class = forms_dict.get(form_pass_class)
    edit_pass = pass_class.objects.get(pk=pk)
    if request.method == "POST":
        form = form_pass_class(request.POST, instance=edit_pass)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = form_pass_class(instance=edit_pass)
    template = 'main\pass\pass_form.html'
    return render(request, template, locals())


def delete_pass(request, pass_pk, pass_class):
    pass_class = passes_class_dict.get(pass_class)
    pass_instance = pass_class.objects.get(pk=pass_pk)

    if request.method == "POST":
        pass_instance.delete()
        return redirect('index')

    template = 'main\pass\\delete_pass.html'
    return render(request, template, locals())


def pass_calendar(request):
    cars_night = Car.objects.order_by('date_of_application_pass_year_night')
    find_actual_passes(cars_night)
    cars_day = Car.objects.order_by('date_of_application_pass_year_day')
    find_actual_passes(cars_day)
    template = 'main\pass\pass_calendar.html'
    return render(request, template, locals())


class OwnerList(ListView):
    model = Owner
    context_object_name = 'owners'
    template_name = 'main\owner\owner_list.html'


class OwnerDetail(DetailView):
    model = Owner
    context_object_name = 'owner'
    template_name = 'main\owner\owner.html'


class AddOwner(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'main\owner\\add_or_update_owner.html'


class UpdateOwner(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'main\owner\\add_or_update_owner.html'


class DeleteOwner(DeleteView):
    model = Owner
    template_name = 'main\owner\\delete_owner.html'
