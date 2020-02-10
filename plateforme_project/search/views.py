from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

#test for login
from django import forms
#from .models import PRODUCTS

def index(request):
   # template = loader.get_template('search/index.html')
    #return HttpResponse(template.render(request=request))
    return render(request, 'search/index.html')


""""
def listing(request):
    products = PRODUCTS
    context = {
        'products' : products
    }
    template = loader.get_template('search/listing.html')
    return HttpResponse(template.render(context, request=request))

"""

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
            user = authenticate(request, username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'search/log_in.html', locals())

def log_out(request):
	logout(request)
	return render(request, 'search/index.html')

def sign_up(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username)
            user = User.objects.create_user(username=username, email=None, password=password)  # Nous vérifions si les données sont correctes
            userid = authenticate(request, username=username, password=password)
            if userid:  # Si l'objet renvoyé n'est pas None
                login(request, userid)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'search/sign_up.html', locals())