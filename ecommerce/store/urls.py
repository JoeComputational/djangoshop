from django.urls import path
from . import views
from .views import checkout
app_name = 'store'

urlpatterns = [
     path('', views.all_products, name='all_products'),
    path('checkout/', checkout, name='checkout'),
]