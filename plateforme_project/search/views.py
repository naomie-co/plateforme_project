from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from search.models import op_food, substitute

"""Views of the pur beurre website"""


def index(request):
    """Function that display the home page"""
    return render(request, 'search/index.html')





def products(request):
    """Function to display substitut products if the request is a get
    Registrer a favorite product with a post request if the user is logged """
    if request.method == "GET":
        query = request.GET.get('query')
        if not query:
            products = op_food.objects.all()[:24]
        else:
            query = query.capitalize()
            products = op_food.objects.filter(name__contains=query).order_by('nutriscore')[:6]
            if len(products) == 0:
                message = "Aucun produit ne correspond aux critères de votre recherche"
            else:
                products = [product for product in products]
                print(products)
        title = "Résultats de la recherche : %s"%query
        context = {
            'products': products,
            'title': title
        }
        return render(request, 'search/products.html', context)

    if request.method == "POST":
        try:
            product = request.POST.get('product')
            user = request.POST.get('user')
            prod = op_food.objects.get(id=product)
            user_id = User.objects.get(id=user)
            #print(user, prod.id)
            #print(type(prod))
            print(product, user)
            selection = substitute.objects.get_or_create(id_substitute=prod, user=user_id)
            message = "Le produit est sauvegardé!"
        except IntegrityError:
            error = True
        return redirect('search:my_selection', user=user)


def detail(request, product_id):
    """Function that display the detail page of a product"""
    product = get_object_or_404(op_food, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'search/detail.html', context)


def my_selection(request, user):
    """Function to display the favorite products of a connected user"""

    if request.user.is_authenticated:
        userid = User.objects.get(id=user)

        subs = substitute.objects.filter(user=userid)

        subs = [elt.id_substitute.id for elt in subs]

        products = [op_food.objects.filter(id=sub)[0] for sub in subs]

        context = {
            'products': products,
        }

        return render(request, 'search/my_selection.html', context)
    else:

        return redirect('account:log_in')


