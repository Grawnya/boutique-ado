from django.http import HttpResponse


class StripeWH_Handler:
    '''Handles stripe webhooks'''

    def __init__(self, request):
        '''to access any attributes of the request coming from stripe'''
        self.request = request

    def handle_event(self, event):
        '''handle a generic/unknown/unexpected webhook event'''

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        '''handle payment_intent.succeeded webhook event'''

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        '''handle payment_intent.payment_failed webhook event'''

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)