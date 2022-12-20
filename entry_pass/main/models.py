from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from datetime import datetime, timedelta


class Owner(models.Model):
    name = models.CharField('Имя', max_length=50)
    contacts = models.CharField('Контакты', max_length=255, blank=True, null=True)
    info = models.TextField('Инофрмация', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('owner', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars',
                             verbose_name='Пользователь', blank=True,
                             null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, related_name='cars',
                              verbose_name='Владелец ТС', blank=True,
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

    # дневные годовые
    can_update_pass_year_day = models.BooleanField('Можно продлить годовой дневной', blank=True, default=False)
    date_of_application_pass_year_day = models.DateField('Дата подачи заявки на годовой дневной', blank=True,
                                                         null=True)
    requested_year_day_pass = models.BooleanField('Подал заявку на годовой дневной', blank=True, default=False)
    date_new_pass_year_day = models.DateField('Дата продления годового дневного', blank=True,
                                              null=True)

    # ночные годовые
    can_update_pass_year_night = models.BooleanField('Можно продлить годовой ночной', blank=True, default=False)
    date_of_application_pass_year_night = models.DateField('Дата подачи заявки на годовой ночной', blank=True,
                                                           null=True)
    requested_year_night_pass = models.BooleanField('Подал заявку на годовой ночной', blank=True, default=False)
    date_new_pass_year_night = models.DateField('Дата продления годового ночного', blank=True,
                                                null=True)

    # разовые
    can_update_pass_one_time = models.BooleanField('Можно продлить разовый', blank=True, default=False)
    date_of_application_pass_one_time = models.DateField('Дата подачи заявки на разовый', blank=True,
                                                         null=True)
    requested_pass_one_time = models.BooleanField('Подал заявку на разовый', blank=True, default=False)

    # проверка годового дневного
    def check_pass_year_day(self):
        if PassDayYear.objects.filter(car=self.pk).count():
            pass_year_day = PassDayYear.objects.filter(car=self.pk).order_by('-end').first()
            self.date_of_application_pass_year_day = pass_year_day.end + timedelta(days=-80)
            if self.date_of_application_pass_year_day <= datetime.now().date():
                self.can_update_pass_year_day = True
            else:
                self.can_update_pass_year_day = False
            self.date_new_pass_year_day = pass_year_day.end + timedelta(days=1)
        else:
            self.can_update_pass_year_day = True
            self.date_of_application_pass_year_day = datetime.now().date()
            self.date_new_pass_year_day = None
        self.save()

    # проверка годового ночного
    def check_pass_year_night(self):
        # если есть ночной
        if PassNightYear.objects.filter(car=self.pk).count():
            pass_year_night = PassNightYear.objects.filter(car=self.pk).order_by('-end').first()
            self.date_of_application_pass_year_night = pass_year_night.end + timedelta(days=-80)
            if self.date_of_application_pass_year_night <= datetime.now().date():
                self.can_update_pass_year_night = True
            else:
                self.can_update_pass_year_night = False
            self.date_new_pass_year_night = pass_year_night.end + timedelta(days=1)
        else:
            self.can_update_pass_year_night = True
            self.date_of_application_pass_year_night = datetime.now().date()
        self.save()

    # проверка разового
    def check_passes_one_time(self):
        if PassOneTime.objects.filter(car=self.pk).count():
            count_one_time_passes = PassOneTime.objects.filter(car=self.pk).count()

            # если создана первая запись
            if count_one_time_passes == 1:
                self.can_update_pass_one_time = True
                self.date_of_application_pass_one_time = PassOneTime.objects.get(car=self.pk).end + timedelta(days=1)
            elif count_one_time_passes > 1:
                penultimate_pass_one_time = PassOneTime.objects.filter(car=self.pk).order_by('-end')[:2][1]
                if penultimate_pass_one_time.end + timedelta(days=30) > datetime.now().date():
                    self.can_update_pass_one_time = False
                else:
                    self.can_update_pass_one_time = True
                self.date_of_application_pass_one_time = penultimate_pass_one_time.end + timedelta(days=32)
        else:
            self.can_update_pass_one_time = True
            self.date_of_application_pass_one_time = datetime.now().date()

        self.save()

    def update_passes_status(self):
        self.check_pass_year_day()
        self.check_pass_year_night()
        self.check_passes_one_time()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Pass(models.Model):
    start = models.DateField('Дата начала', blank=True, null=True)
    end = models.DateField('Дата окончания', blank=True, null=True)
    current = models.BooleanField('Действующий', default=True)
    canceled = models.BooleanField('Аннулирован', default=False)


class PassDayYear(Pass):
    title = models.CharField(default='Годовой дневной пропуск', max_length=20, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='year_day_passes',
                            verbose_name='ТС', blank=True,
                            null=True)

    def __str__(self):
        return f'pass_day_year_{self.start}-{self.end}'

    def get_absolute_url(self):
        return reverse('pass_day_year', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Годовой дневной пропуск'
        verbose_name_plural = 'Годовые дневные пропуски'
        ordering = ['-end']


class PassNightYear(Pass):
    title = models.CharField(default='Годовой ночной пропуск', max_length=20, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='year_night_passes',
                            verbose_name='ТС', blank=True,
                            null=True)

    def __str__(self):
        return f'pass_night_year_{self.start}-{self.end}'

    def get_absolute_url(self):
        return reverse('pass_night_year', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Годовой ночной пропуск'
        verbose_name_plural = 'Годовые ночные пропуски'
        ordering = ['-end']


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
        ordering = ['-end']
