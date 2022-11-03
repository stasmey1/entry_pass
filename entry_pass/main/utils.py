from .models import *
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=PassOneTime)
def get_date_extended_one_time_pass(sender, instance, created, **kwargs):
    car = Car.objects.get(one_time_passes=instance)
    n = PassOneTime.objects.filter(car=car).count()
    one_time_passes = PassOneTime.objects.filter(car=car)[:n]
    if one_time_passes.count() >= 1:
        ### нужно понять как вытащить предпоследнюю запись     ###
        car.date_extended_pass_one_time = one_time_passes.last().end + timedelta(days=31)
    else:
        car.date_extended_pass_one_time = datetime.now().date()
