from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.template import loader
from search.models import categorie, op_food, substitute

#test for login
from django import forms
#from .models import PRODUCTS

def index(request):
    return render(request, 'search/index.html')


#log-in test
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

def log_in(request):

    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            else: # error message
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'search/log_in.html', locals())


def log_out(request):
	logout(request)
	return render(request, 'search/index.html')


def sign_up(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.create_user(username=username, email=None, password=password)
                userid = authenticate(request, username=username, password=password)
                login(request, userid)
            except IntegrityError: 
                error = True #variable to print an error message if the username already exists
                form = ConnexionForm()
    else:
        form = ConnexionForm()
    return render(request, 'search/sign_up.html', locals())


def products(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if not query:
            products = op_food.objects.all()[:24]

        else:
            products = op_food.objects.filter(name__icontains=query)[:6]
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
    if request.method == "POST":
        try:
            product = request.POST.get('product')
            user = request.POST.get('user')
            #prod = op_food.objects.get(id=product)
            #user_name = User.objects.get(username=user)
            #print(user, prod.id)
            #print(type(prod))
            print(product, user)
            selection = substitute.objects.create(id_substitute=product, user=user)
            message = "Le produit est sauvegardé!"
        except IntegrityError:
            error = True
        context = {
        'message': message
        }  

    return render(request, 'search/products.html', context)


def detail(request, product_id):

    product = op_food.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'search/detail.html', context)


def my_selection (request, user):

    userid = User.objects.get(id=user)

    subs = substitute.objects.filter(user=userid)

    subs = [subs.id_substitute for elt in subs]

    products = [op_food.objects.filter(id=sub) for sub in subs]

    products = [product for product in products]

    context = {
        'products': products,
    }

    return render(request, 'search/my_selection.html', context)



