from django.urls import path
from asset_management import views

urlpatterns = [
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:device_id>/checkout/', views.checkout_device, name='checkout_device'),
    path('devices/<int:device_id>/return/', views.return_device, name='return_device'),
]
