import random
import string

from django.core.mail import send_mail

from entry_pass.celery import app
from entry_pass.settings import EMAIL_HOST_USER
from .models import Car


def email_notification(car: Car):
    send_mail(subject='напоминание по пропускам',
              message=f'наступила дата подачи на пропуск {car.register_number}',
              from_email=EMAIL_HOST_USER,
              recipient_list=[EMAIL_HOST_USER, ])


@app.task
def check_cars(cars: list):
    for car in cars:
        car = car.update_passes_status()
        if car.requested_year_day_pass:
            email_notification(car)
