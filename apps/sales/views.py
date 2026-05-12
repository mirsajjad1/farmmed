from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.medicines.models import Medicine
from .models import Sale, SaleItem
from django.contrib import messages
from django.http import JsonResponse
from datetime import date
# Create your views here.


@login_required
def sales_history(request):
    filter_type = request.GET.get('filter')
    sales = Sale.objects.all()

    if filter_type == 'today':
        today = date.today()
        sales = sales.filter(created_at__date=today)

    sales = sales.order_by('-created_at')

    return render(request, 'sales/history.html', {'sales': sales})



@login_required
def sales_history(request):
    sales = Sale.objects.all().order_by('-created_at')

    return render(request, 'sales/history.html', {'sales': sales})

@login_required
def create_sale(request):
    medicines = Medicine.objects.all()

    if request.method == 'POST':
        import json
        data = json.loads(request.body)

        sale = Sale.objects.create(created_by=request.user)
        total = 0

        for item in data:
            medicine = Medicine.objects.get(id=item['id'])
            qty = int(item['qty'])

            if medicine.stock < qty:
                return JsonResponse({'error': f"Not enough stock for {medicine.name}"})

            price = medicine.price
            purchase_price = medicine.purchase_price

            total += price * qty

            # update stock
            medicine.stock -= qty
            medicine.save()

            SaleItem.objects.create(
                sale=sale,
                medicine=medicine,
                quantity=qty,
                price=price,
                purchase_price=purchase_price
            )

        sale.total_amount = total
        sale.save()

        return JsonResponse({'success': True, 'sale_id': sale.id})

    return render(request, 'sales/pos.html', {'medicines': medicines})


# @login_required
# def create_sale(request):
#     medicines = Medicine.objects.all()

#     if request.method == 'POST':
#         medicine_ids = request.POST.getlist('medicine')
#         quantities = request.POST.getlist('quantity')

#         sale = Sale.objects.create(created_by=request.user)
#         total = 0

#         for med_id, qty in zip(medicine_ids, quantities):
#             if not qty or int(qty) <= 0:
#                 continue

#             medicine = Medicine.objects.get(id=med_id)
#             qty = int(qty)

#             # ❗ STOCK CHECK
#             if medicine.stock < qty:
#                 messages.error(request, f"Not enough stock for {medicine.name}")
#                 sale.delete()
#                 return redirect('create_sale')

#             # 💰 Calculate
#             price = medicine.price
#             purchase_price = medicine.purchase_price
#             total += price * qty

#             # 🔻 UPDATE STOCK
#             medicine.stock -= qty
#             medicine.save()

#             # 🧾 Create SaleItem
#             SaleItem.objects.create(
#                 sale=sale,
#                 medicine=medicine,
#                 quantity=qty,
#                 price=price,
#                 purchase_price=purchase_price
# )
#         sale.total_amount = total
#         sale.save()

#         messages.success(request, "Sale completed successfully")
#         return redirect('sale_receipt', sale.id)

#     return render(request, 'sales/create_sale.html', {'medicines': medicines})

def sale_receipt(request, sale_id):
    sale = Sale.objects.get(id=sale_id)
    return render(request, 'sales/receipt.html', {'sale': sale})