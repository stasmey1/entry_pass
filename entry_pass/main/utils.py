import datetime

from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=PassDayYear)
def update_data_car(sender, instance, created, **kwargs):
    car = Car.objects.get(year_day_passes=instance)
    car.update_passes_status()


@receiver(post_save, sender=PassNightYear)
def update_data_car(sender, instance, created, **kwargs):
    car = Car.objects.get(year_night_passes=instance)
    car.update_passes_status()


@receiver(post_save, sender=PassOneTime)
def update_data_car(sender, instance, created, **kwargs):
    car = Car.objects.get(one_time_passes=instance)
    car.update_passes_status()


def find_actual_passes(cars):
    for car in cars:
        car.pass_year_day = PassDayYear.objects.filter(car=car).first() if PassDayYear.objects.filter(
            car=car).count() else None
        if car.pass_year_day is not None:
            car.pass_year_day_residue = car.pass_year_day.end - datetime.now().date()
        car.pass_year_night = PassNightYear.objects.filter(car=car).first() if PassNightYear.objects.filter(
            car=car).count() else None
        if car.pass_year_night is not None:
            car.pass_year_night_residue = car.pass_year_night.end - datetime.now().date()
