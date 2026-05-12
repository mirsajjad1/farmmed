from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from datetime import date

from apps.medicines.models import Medicine
from apps.sales.models import Sale


# Create your views here.

@login_required
def dashboard(request):
    # 📦 Medicine stats
    total_medicines = Medicine.objects.count()
    total_stock = Medicine.objects.aggregate(Sum('stock'))['stock__sum'] or 0
    low_stock = Medicine.objects.filter(stock__lt=10)

    # 📅 Dates
    today = date.today()

    # 💰 Today sales
    today_sales = Sale.objects.filter(created_at__date=today)
    today_total = today_sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    today_count = today_sales.count()

    today_profit = today_sales.aggregate(
        profit=Sum((F('items__price') - F('items__purchase_price')) * F('items__quantity')))['profit'] or 0


    # 📆 Monthly sales
    month_sales = Sale.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month
    )
    month_total = month_sales.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    month_count = month_sales.count()

    month_profit = month_sales.aggregate(
        profit=Sum((F('items__price') - F('items__purchase_price')) * F('items__quantity')))['profit'] or 0

    context = {
        'total_medicines': total_medicines,
        'total_stock': total_stock,
        'low_stock': low_stock,

        'today_total': today_total,
        'today_count': today_count,

        'month_total': month_total,
        'month_count': month_count,

        'today_profit': today_profit,
        'month_profit': month_profit,
    }

    return render(request, 'dashboard/index.html', context)