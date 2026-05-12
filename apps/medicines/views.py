from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicine
from .forms import MedicineForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
# Create your views here.
@login_required
def add_medicine(request):
    form = MedicineForm(request.POST or None)

    if form.is_valid():
        medicine = form.save(commit=False)
        medicine.user = request.user
        medicine.save()
        return redirect('medicine_list')

    return render(request, 'medicines/add.html', {'form': form})

@login_required
def medicine_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    medicines = Medicine.objects.all()

    if query:
        medicines = medicines.filter(name__icontains=query)

    if category:
        medicines = medicines.filter(category__icontains=category)

    return render(request, 'medicines/list.html', {'medicines': medicines})

   

@login_required
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    form = MedicineForm(request.POST or None, instance=medicine)

    if form.is_valid():
        form.save()
        return redirect('medicine_list')

    return render(request, 'medicines/edit.html', {'form': form})



@login_required
def delete_medicine(request, pk):
    # 🔐 Role check
    if request.user.role != 'admin':
        messages.error(request, "You are not allowed to delete")
        return redirect('medicine_list')
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')

    return render(request, 'medicines/delete.html', {'medicine': medicine})