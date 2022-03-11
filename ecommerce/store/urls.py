from django.urls import include, path
from . import views
from .views import checkout, success, cancel, index
app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('index/', index, name='index'),
]

#These are the internal url pathing, I need to set up another within store as well