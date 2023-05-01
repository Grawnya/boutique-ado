from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {}) # get the shopping bag
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N2fW4EVxEJFT91WjxVyEVJW7JKQa4SByO5Pr1TugsdNlJHjVaxpMmzHhxPkVIVSnNw8QpzwY1fvisnr9MVqUYmn00YUPFKBaM',
        'client_secret': 'test client secret'
    }
    return render(request, template, context)