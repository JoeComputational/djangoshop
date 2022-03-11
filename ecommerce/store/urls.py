from django.urls import path
from . import views
from .views import checkout, success, cancel
app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]