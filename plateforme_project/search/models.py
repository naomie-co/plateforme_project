from django.db import models
from django.contrib.auth.models import User

"""
#list to test models
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

class categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class op_food(models.Model):
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    ingredient = models.CharField(max_length=2000)
    nutritional_values = models.CharField(max_length=100)
    url = models.URLField()
    picture = models.URLField(null=True)
    picture_100g = models.URLField(null=True)
    categorie = models.ForeignKey(categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class substitute(models.Model):
    id_substitute = models.ForeignKey(op_food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.id, self.id_substitute.id
