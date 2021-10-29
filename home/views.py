from products.models import Product

def index(request):
    """A view to return to the index page"""

    products =Product.objects.all()
    selected_products = list(products.slice(3))
    print(selected_products)

    context = {
        'product': product,
    }

    return render(request, 'home/index.html')