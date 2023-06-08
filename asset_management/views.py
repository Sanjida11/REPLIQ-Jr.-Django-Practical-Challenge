from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company, Employee, Device
from .forms import CheckoutForm, ReturnForm


@login_required
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'asset_management/device_list.html', {'devices': devices})


@login_required
def checkout_device(request, device_id):
    device = Device.objects.get(id=device_id)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            device.checked_out_by = employee
            device.checked_out_date = form.cleaned_data['checked_out_date']
            device.condition = form.cleaned_data['condition']
            device.save()
            return redirect('device_list')
    else:
        form = CheckoutForm()

    return render(request, 'asset_management/checkout_device.html', {'form': form, 'device': device})


@login_required
def return_device(request, device_id):
    device = Device.objects.get(id=device_id)

    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            device.returned_date = form.cleaned_data['returned_date']
            device.returned_condition = form.cleaned_data['returned_condition']
            device.save()
            return redirect('device_list')
    else:
        form = ReturnForm()

    return render(request, 'asset_management/return_device.html', {'form': form, 'device': device})
