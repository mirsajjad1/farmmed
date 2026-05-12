from django.db import models
from apps.medicines.models import Medicine
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL

class Sale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_amount = models.FloatField(default=0)

    def __str__(self):
        return f"Sale #{self.id}"
class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    price = models.FloatField()           # selling price at sale time
    purchase_price = models.FloatField()  # cost price at sale time

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"