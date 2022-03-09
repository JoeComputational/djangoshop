from django.shortcuts import render, redirect
import stripe
from django.conf import settings


def index(request):
    return render(request, 'index.html')


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
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/success',
    )
    
    return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, "../templaces/store/success.html", None)
