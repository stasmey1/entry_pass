from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='index'),

    path('owner_list/', OwnerList.as_view(), name='owner_list'),
    path('add_owner/', AddOwner.as_view(), name='add_owner'),
    path('owner/<int:pk>/', OwnerDetail.as_view(), name='owner'),
    path('update_owner/<int:pk>/', UpdateOwner.as_view(), name='update_owner'),
    path('delete_owner/<int:pk>/', DeleteOwner.as_view(), name='delete_owner'),

    path('add_car/', AddCar.as_view(), name='add_car'),
    path('car/<int:pk>/', DetailCar.as_view(), name='car'),
    path('update_car/<int:pk>/', UpdateCar.as_view(), name='update_car'),
    path('delete_car/<int:pk>/', DeleteCar.as_view(), name='delete_car'),

    path('add_pass_year/<int:pk>/', add_pass_year, name='add_pass_year'),
    path('update_pass_year/<int:pk>/', UpdatePassYear.as_view(), name='update_pass_year'),
    path('delete_pass_year/<int:pk>/', DeletePassYear.as_view(), name='delete_pass_year'),

    path('add_pass_one_time/<int:pk>/', add_pass_one_time, name='add_pass_one_time'),
    path('update_pass_one_time/<int:pk>/', UpdatePassOneTime.as_view(), name='update_pass_one_time'),
    path('delete_pass_one_time/<int:pk>/', DeletePassOneTime.as_view(), name='delete_pass_one_time'),

    path('pass_calendar', pass_calendar, name='pass_calendar'),

]
