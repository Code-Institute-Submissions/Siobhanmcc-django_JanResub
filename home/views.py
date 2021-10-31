from products.models import Product
from django.shortcuts import render

def index(request):
    """A view to return to the index page"""

    products =Product.objects.all()
    products_list = list(products)
    selected_products = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x=slice(3)
    new_list = products_list[x]
    print(new_list)

    context = {
        'new_list': new_list,
    }

    return render(request, 'home/index.html', context)