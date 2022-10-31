from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from .mixins import *


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
        context['passes'] = Pass.objects.filter(car=self.get_object().pk)
        return context


class DeleteCar(DeleteView):
    model = Car
    template_name = 'main\\delete_car.html'
    success_url = '/'


def add_pass(request):
    if request.method == "POST":
        form = PassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PassForm()
    template = 'main\pass_form.html'
    return render(request, template, locals())



class UpdatePass(PassMixin, UpdateView):
    pass


class DetailPass(DetailView):
    model = Pass
    context_object_name = 'pass'
    template_name = 'main\pass.html'


class DeletePass(DeleteView):
    model = Pass
    template_name = 'main\\delete_pass.html'
    success_url = '/'
