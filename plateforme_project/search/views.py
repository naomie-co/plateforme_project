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
                error = True #variable to print an error message il the username already exists
                form = ConnexionForm()
    else:
        form = ConnexionForm()
    return render(request, 'search/sign_up.html', locals())


def products(request):
    query = request.GET.get('query')
    if not query:
        products = op_food.objects.all()

    else:
        products = op_food.objects.filter(name__icontains=query)
        if len(products) == 0:
            message = "Aucun produit ne correspond aux critères de votre recherche"
        else:
            products = [product for product in products]
    title = "Résultats pour la recherche : %s"%query
    context = {
        'products': products,
        'title': title
    }
    return render(request, 'search/products.html', context)


def detail(request, product_id):

    product = op_food.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'search/detail.html', context)


