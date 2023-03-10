# Generated by Django 4.1.3 on 2022-12-16 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('contacts', models.CharField(blank=True, max_length=255, null=True, verbose_name='Контакты')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Инофрмация')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владельцы',
            },
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('current', models.BooleanField(default=True, verbose_name='Действующий')),
                ('canceled', models.BooleanField(default=False, verbose_name='Аннулирован')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование')),
                ('register_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='ГРН')),
                ('vin', models.CharField(blank=True, max_length=20, null=True, verbose_name='VIN')),
                ('sts', models.CharField(blank=True, max_length=10, null=True, verbose_name='СТС')),
                ('sts_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи СТС')),
                ('brand', models.CharField(blank=True, max_length=20, null=True, verbose_name='Марка')),
                ('model', models.CharField(blank=True, max_length=20, null=True, verbose_name='Модель')),
                ('created', models.DateField(blank=True, null=True, verbose_name='Дата выпуска ТС')),
                ('eco_class', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Экологический класс')),
                ('max_weight', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Разрешенная максимальная масса')),
                ('weight_without_load', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Масса без нагрузки')),
                ('number_check_card', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер диагностической карты')),
                ('date_check_card', models.DateField(blank=True, null=True, verbose_name='Срок действия диагностической карты')),
                ('can_update_pass_year_day', models.BooleanField(blank=True, default=False, verbose_name='Можно продлить годовой дневной')),
                ('date_of_application_pass_year_day', models.DateField(blank=True, null=True, verbose_name='Дата подачи заявки на годовой дневной')),
                ('requested_year_day_pass', models.BooleanField(blank=True, default=False, verbose_name='Подал заявку на годовой дневной')),
                ('date_new_pass_year_day', models.DateField(blank=True, null=True, verbose_name='Дата продления годового дневного')),
                ('can_update_pass_year_night', models.BooleanField(blank=True, default=False, verbose_name='Можно продлить годовой ночной')),
                ('date_of_application_pass_year_night', models.DateField(blank=True, null=True, verbose_name='Дата подачи заявки на годовой ночной')),
                ('requested_year_night_pass', models.BooleanField(blank=True, default=False, verbose_name='Подал заявку на годовой ночной')),
                ('date_new_pass_year_night', models.DateField(blank=True, null=True, verbose_name='Дата продления годового ночного')),
                ('can_update_pass_one_time', models.BooleanField(blank=True, default=False, verbose_name='Можно продлить разовый')),
                ('date_of_application_pass_one_time', models.DateField(blank=True, null=True, verbose_name='Дата подачи заявки на разовый')),
                ('requested_pass_one_time', models.BooleanField(blank=True, default=False, verbose_name='Подал заявку на разовый')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='main.owner', verbose_name='Владелец ТС')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='PassOneTime',
            fields=[
                ('pass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.pass')),
                ('title', models.CharField(blank=True, default='Разовый пропуск', max_length=20)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='one_time_passes', to='main.car', verbose_name='Транспортное средство')),
            ],
            options={
                'verbose_name': 'Разовый пропуск',
                'verbose_name_plural': 'Разовые пропуски',
                'ordering': ['-end'],
            },
            bases=('main.pass',),
        ),
        migrations.CreateModel(
            name='PassNightYear',
            fields=[
                ('pass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.pass')),
                ('title', models.CharField(blank=True, default='Годовой ночной пропуск', max_length=20)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='year_night_passes', to='main.car', verbose_name='ТС')),
            ],
            options={
                'verbose_name': 'Годовой ночной пропуск',
                'verbose_name_plural': 'Годовые ночные пропуски',
                'ordering': ['-end'],
            },
            bases=('main.pass',),
        ),
        migrations.CreateModel(
            name='PassDayYear',
            fields=[
                ('pass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.pass')),
                ('title', models.CharField(blank=True, default='Годовой дневной пропуск', max_length=20)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='year_day_passes', to='main.car', verbose_name='ТС')),
            ],
            options={
                'verbose_name': 'Годовой дневной пропуск',
                'verbose_name_plural': 'Годовые дневные пропуски',
                'ordering': ['-end'],
            },
            bases=('main.pass',),
        ),
    ]
