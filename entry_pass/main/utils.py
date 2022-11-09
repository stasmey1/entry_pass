from .models import *
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


# Определение даты продления разового пропуска
@receiver(post_save, sender=PassOneTime)
def get_date_extended_one_time_pass(sender, instance, created, **kwargs):
    car = Car.objects.get(one_time_passes=instance)
    count_one_time_passes = PassOneTime.objects.filter(car=car).count()

    # если создана первая запись
    if count_one_time_passes == 1:
        car.date_of_application_pass_one_time = PassOneTime.objects.get(car=car).end + timedelta(days=1)
        car.save()
    else:
        penultimate_pass = PassOneTime.objects.filter(car=car).order_by('-end')[:2][1]
        car.date_of_application_pass_one_time = penultimate_pass.end + timedelta(days=32)
        car.save()


# Определение даты продления годового пропуска
@receiver(post_save, sender=PassYear)
def get_date_extended_pass_year(sender, instance, created, **kwargs):
    car = Car.objects.get(year_passes=instance)

    # если пропуск дневной:
    if instance.times_of_day == 'day':
        car.date_of_application_pass_year_day = instance.end + timedelta(days=-80)
        car.save()
    else:
        car.date_of_application_pass_year_night = instance.end + timedelta(days=-80)
        car.save()
