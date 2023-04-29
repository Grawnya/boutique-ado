from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem # where OrderLineItem is the sender

# to execute this function any time the post save signal is sent, use the receiver decorator
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    '''
    update order total on lineitem update/create
    '''
    # instance.order refers to the order that the specific line item is related to
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    '''
    update order total on lineitem delete
    '''
    instance.order.update_total()