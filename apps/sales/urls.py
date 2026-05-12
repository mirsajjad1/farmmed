
from django.urls import path
from .views import create_sale, sale_receipt, sales_history

urlpatterns = [
    path('create/', create_sale, name='create_sale'),
    path('receipt/<int:sale_id>/', sale_receipt, name='sale_receipt'),
    path('pos/', create_sale, name='pos'),
    path('history/', sales_history, name='sales_history'),
]