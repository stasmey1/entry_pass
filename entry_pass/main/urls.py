from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('car/<int:pk>/', DetailCar.as_view(), name='car'),
    path('add_car/', AddCar.as_view(), name='add_car'),
    path('update_car/<int:pk>/', UpdateCar.as_view(), name='update_car'),
    path('delete_car/<int:pk>/', DeleteCar.as_view(), name='delete_car'),

    path('pass_year/<int:pk>/', DetailPassYear.as_view(), name='pass_year'),
    path('add_pass_year/', AddPassYear.as_view(), name='add_pass_year'),
    path('update_pass_year/<int:pk>/', UpdatePassYear.as_view(), name='update_pass_year'),
    path('delete_pass_year/<int:pk>/', DeletePassYear.as_view(), name='delete_pass_year'),

]
