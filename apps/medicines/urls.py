
from django.urls import path
from .views import medicine_list, add_medicine, edit_medicine, delete_medicine

urlpatterns = [
    path('', medicine_list, name='medicine_list'),
    path('add/', add_medicine, name='add_medicine'),
    path('edit/<int:pk>/', edit_medicine, name='edit_medicine'),
    path('delete/<int:pk>/', delete_medicine, name='delete_medicine'),
]
