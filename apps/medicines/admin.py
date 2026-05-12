from django.contrib import admin
from .models import Medicine
# Register your models here.

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    search_fields = ('name', 'category')
    list_filter = ('category',)

admin.site.register(Medicine, MedicineAdmin)