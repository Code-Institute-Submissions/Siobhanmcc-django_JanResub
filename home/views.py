from products.models import Product
from django.shortcuts import render

def index(request):
    """A view to return to the index page"""

    Product.objects.all().order_by('-sold_items')[:3]


    products =Product.objects.all()
    products_list = list(products)
    x=slice(3)
    new_list = products_list[x]
    print(new_list)

    context = {
        'new_list': new_list,
    }

    return render(request, 'home/index.html', context)