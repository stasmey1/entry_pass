from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from datetime import datetime, timedelta


class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars',
                             verbose_name='Пользователь', blank=True,
                             null=True)
    name = models.CharField('Наименование', max_length=30)
    register_number = models.CharField('ГРН', max_length=10, blank=True, null=True)
    vin = models.CharField('VIN', max_length=20, blank=True, null=True)
    sts = models.CharField('СТС', max_length=10, blank=True, null=True)
    sts_date = models.DateField('Дата выдачи СТС', blank=True, null=True)
    brand = models.CharField('Марка', max_length=20, blank=True, null=True)
    model = models.CharField('Модель', max_length=20, blank=True, null=True)
    created = models.DateField('Дата выпуска ТС', blank=True, null=True)
    eco_class = models.PositiveSmallIntegerField('Экологический класс', blank=True, null=True)
    max_weight = models.PositiveSmallIntegerField('Разрешенная максимальная масса', blank=True, null=True)
    weight_without_load = models.PositiveSmallIntegerField('Масса без нагрузки', blank=True, null=True)
    number_check_card = models.CharField('Номер диагностической карты', max_length=20, blank=True, null=True)
    date_check_card = models.DateField('Срок действия диагностической карты', blank=True, null=True)

    date_extended_pass_year = models.DateField('Можно продлить годовой пропуск', blank=True, null=True)
    date_extended_pass_one_time = models.DateField('Можно продлить разовый пропуск', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Pass(models.Model):
    TIMES_OF_DAY = (
        ('day', 'Дневной'),
        ('night', 'Ночной')
    )

    times_of_day = models.CharField('Вид', max_length=10, choices=TIMES_OF_DAY, null=True)
    start = models.DateField('Дата начала', blank=True, null=True)
    end = models.DateField('Дата окончания', blank=True, null=True)
    current = models.BooleanField('Действующий', default=True)
    canceled = models.BooleanField('Аннулирован', default=False)

    class Meta:
        verbose_name = 'Пропуск'
        verbose_name_plural = 'Пропуски'


class PassYear(Pass):
    title = models.CharField(default='Годовой пропуск', max_length=20, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='year_passes',
                            verbose_name='Транспортное средство', blank=True,
                            null=True)

    def __str__(self):
        return f'pass_year_{self.times_of_day}_{self.start}- {self.end}'

    def get_absolute_url(self):
        return reverse('pass_year', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Годовой пропуск'
        verbose_name_plural = 'Годовые пропуски'


class PassOneTime(Pass):
    title = models.CharField(default='Разовый пропуск', max_length=20, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='one_time_passes',
                            verbose_name='Транспортное средство', blank=True,
                            null=True)

    def __str__(self):
        return f'pass_one_time_{self.times_of_day}_{self.start}- {self.end}'

    def get_absolute_url(self):
        return reverse('pass_one_time', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Разовый пропуск'
        verbose_name_plural = 'Разовые пропуски'
