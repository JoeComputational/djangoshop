from django.shortcuts import render, redirect
from .models import Category, Product
import stripe
import dotenv
from django.conf import settings

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def index(request):
    return render(request, '../templates/store/index.html')

stripe.api_key = 'sk_test_51KbFLTIqGVD2vOHKHV9fRXfpId64cxto2m7wiVebcWdXeNZOWK40fDw5CIHeHWOmtmcGqlbmQoSqOe9cAxhQJ8mm00iQucHl40'


def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # This is the product ID for kidneyh beans
                'price': 'price_1KbFf8IqGVD2vOHKLVALlQMd',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://3.26.206.173:8000/success',
        cancel_url='http://3.26.206.173:8000/cancel',
    )
    return redirect(checkout_session.url, code=303)
#This is directly from Stripe, this is to include their purchase portal
#Its also to record purchases on our Database


#This is the successful purchase routing of the application

def success(request):
    return render(request, "../templates/store/success.html", None)


#This is the cancelled purchase request routing of the application
def cancel(request):
    return render(request, "../templates/store/cancel.html", None)
