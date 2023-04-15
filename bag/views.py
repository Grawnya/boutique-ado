from django.shortcuts import render, redirect


def view_bag(request):
    '''
    A view to return the shopping bag page
    '''
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    '''
    Add a quantity of the specified product to the shopping bag.
    '''
    quantity = int(request.POST.get('quantity')) # int as will come from template as string
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    # used to track different IDs for items ordered that have a different size but are the same product
    if size:
        if item_id in list(bag.keys()):
            # checks if item with the same size and if exists
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            # add as specific quantity for the item with a different size
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    # if the item doesn't have a size
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)