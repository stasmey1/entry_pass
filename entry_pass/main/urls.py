from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),

    path('car/<int:pk>/', DetailCar.as_view(), name='car'),
    path('add_car/', AddCar.as_view(), name='add_car'),
    path('update_car/<int:pk>/', UpdateCar.as_view(), name='update_car'),
    path('delete_car/<int:pk>/', DeleteCar.as_view(), name='delete_car'),

    path('pass/<int:pk>/', DetailPass.as_view(), name='pass'),
    path('add_pass/', add_pass, name='add_pass'),
    path('update_pass/<int:pk>/', UpdatePass.as_view(), name='update_pass'),
    path('delete_pass/<int:pk>/', DeletePass.as_view(), name='delete_pass'),

]
