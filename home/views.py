from products.models import Product
from django.shortcuts import render

def index(request):
    """A view to return to the index page"""

    products = Product.objects.all().order_by('-sold_items')[:3]

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)