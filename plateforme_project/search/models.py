from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
PRODUCTS = [
    {'name': 'coca-cola', 'type': 'boisson'},
    {'name': 'eau', 'type': 'boisson'},
    {'name': 'chips', 'type': 'snack'},
    {'name': 'fanta', 'type': 'boisson'},
    {'name': 'vita-coco', 'type': 'boisson'},
    {'name': 'mini-pizza', 'type': 'snack'},
    {'name': 'jus de pomme', 'type': 'boisson'},
    {'name': 'café', 'type': 'boisson'},
    {'name': 'crackers', 'type': 'snack'},
]
"""

class categories(models.Model):
    categorie = models.CharField(max_length=100)

class op_food(models.Model):
    nom = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    ingredients = models.CharField(max_length=255)
    store = models.CharField(max_length=100)
    url = models.URLField()
    id_categorie = models.OneToOneField(categories, on_delete=models.CASCADE)


class substitute(models.Model):
    #id_original = models.ForeignKey(op_food, on_delete=models.CASCADE)
    id_substitute = models.ForeignKey(op_food, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="substitute", blank=True)
