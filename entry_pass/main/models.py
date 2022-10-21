from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.conf import settings


class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars', blank=True,
                             null=True)
    name = models.CharField(max_length=30)
    register_number = models.CharField(max_length=10, blank=True, null=True)
    vin = models.CharField(max_length=20, blank=True, null=True)
    sts = models.CharField(max_length=10, blank=True, null=True)
    sts_date = models.DateField(blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    eco_class = models.PositiveSmallIntegerField(blank=True, null=True)
    max_weight = models.PositiveSmallIntegerField(blank=True, null=True)
    weight_without_load = models.PositiveSmallIntegerField(blank=True, null=True)
    number_check_card = models.CharField(max_length=20, blank=True, null=True)
    date_check_card = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Pass(models.Model):
    TIMES_OF_DAY = (
        ('day', 'day'),
        ('night', 'night')
    )

    times_of_day = models.CharField(max_length=10, choices=TIMES_OF_DAY)
    start = models.DateField(blank=True, default=timezone.now().date())
    end = models.DateField(blank=True, null=True)
    can_be_used = models.DateField(blank=True, null=True)
    current = models.BooleanField('Действующий', default=True)
    canceled = models.BooleanField('Аннулирован', default=False)

    def __str__(self):
        return f'_{self.start}- {self.end}_{self.times_of_day}'

    def get_absolute_url(self):
        return reverse('pass', kwargs={'pk':self.pk})


class PassYear(Pass, models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='pass_year', null=True)

    def __str__(self):
        return f'Годовой пропуск_{self.car}' + super().__str__()

    class Meta:
        verbose_name = 'Годовой пропуск'
        verbose_name_plural = 'Годовые пропуски'


class PassTenDays(Pass, models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='pass_ten_days', null=True)

    def __str__(self):
        return f'Разовый пропуск_{self.car}' + super().__str__()

    class Meta:
        verbose_name = 'Разовый пропуск'
        verbose_name_plural = 'Разовые пропуски'
