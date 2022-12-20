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
