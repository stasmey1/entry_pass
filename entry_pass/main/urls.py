from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('update_passes_status/', update_passes_status, name='update_passes_status'),

    path('owner_list/', OwnerList.as_view(), name='owner_list'),
    path('add_owner/', AddOwner.as_view(), name='add_owner'),
    path('owner/<int:pk>/', OwnerDetail.as_view(), name='owner'),
    path('update_owner/<int:pk>/', UpdateOwner.as_view(), name='update_owner'),
    path('delete_owner/<int:pk>/', DeleteOwner.as_view(), name='delete_owner'),

    path('add_car/', AddCar.as_view(), name='add_car'),
    path('car/<int:pk>/', DetailCar.as_view(), name='car'),
    path('update_car/<int:pk>/', UpdateCar.as_view(), name='update_car'),
    path('delete_car/<int:pk>/', DeleteCar.as_view(), name='delete_car'),

    path('add_pass_day_year/<int:pk_car>/', add_pass, {'form_pass_class': 'PassDayYearForm'}, name='add_pass_day_year'),

    path('add_pass_night_year/<int:pk_car>/', add_pass, {'form_pass_class': 'PassNightYearForm'},
         name='add_pass_night_year'),

    path('add_pass_one_time/<int:pk_car>/', add_pass, {'form_pass_class': 'PassOneTimeForm'}, name='add_pass_one_time'),

    path('update_pass_day_year/<int:pk>/', update_pass,
         {'form_pass_class': 'PassDayYearForm',
          'pass_class': 'PassDayYear'},
         name='update_pass_day_year'),

    path('update_pass_night_year/<int:pk>/', update_pass,
         {'form_pass_class': 'PassNightYearForm',
          'pass_class': 'PassNightYear'},
         name='update_pass_night_year'),

    path('update_pass_one_time/<int:pk_car>/', update_pass, {'form_pass_class': 'PassOneTimeForm',
                                                             'pass_class': 'PassOneTime'}, name='update_pass_one_time'),

    path('delete_pass_day_year/<int:pass_pk>/', delete_pass, {'pass_class': 'PassDayYear'},
         name='delete_pass_day_year'),

    path('delete_pass_night_year/<int:pass_pk>/', delete_pass, {'pass_class': 'PassNightYear'},
         name='delete_pass_night_year'),

    path('delete_pass_one_time/<int:pass_pk>/', delete_pass, {'pass_class': 'PassOneTime'},
         name='delete_pass_one_time'),

    path('pass_calendar/', pass_calendar, name='pass_calendar'),

]
