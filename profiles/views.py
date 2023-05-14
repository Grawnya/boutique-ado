from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import *

def profile(request):
    '''display user profile'''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updates successfully')

        else:
            messages.error(request, 'Update failed. Please ensure that the form is valid')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all() # gets user's orders

    template = 'profiles/profile.html'
    context = {
        'form':form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'This is a past order confirmation for order number {order_number}'
                            'A confirmation email was sent on the order date')
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile' : True, # added to check in the template if the user they were on their profile page before checkout so the user can be redirected back if the payment is successful
    }

    return render(request, template, context)