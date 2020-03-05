import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from search.models import categorie, op_food
from search.const import CATEGORIES



class Command(BaseCommand):
    """This class aims to interact with the OpenfoodFact's API
    Its parameters aims to prepared the request
    Its request_product method made the resquest
    """
    def __init__(self):
        """Parameters for the API request"""
        self.url = 'https://world.openfoodfacts.org/cgi/search.pl'
        self.param = {
            'action':'process',
            'tagtype_0':'categories',
            'tag_contains_0':'contains',
            'tag_0':'',
            'page_size':50,
            'json':1
        }

    def categorie_db(self):
        """Insert categories into .models categorie's table"""
        for elt in CATEGORIES:
            cat = categorie()
            cat.name = elt
            #cat.clean()
            #print("Zero print : ", elt)
            cat.save()
        return cat


    def request_product(self, tag):
        """Get products from the API depending on the tag in parameter.
        Store the result in a list of list named data
        Return data """
        i = 0
        self.param["tag_0"] = tag
        request = requests.get(self.url, params=self.param)
        result = request.json()
        data = []
        for val in result["products"]:
            try:
                data.append([val["product_name_fr"],\
                val["nutrition_grades"], val["ingredients_text_fr"],\
                val["image_nutrition_url"], val["image_url"], val["url"]])
                i += 1
                if i > 40:
                    break
            except KeyError:
                pass
        #print("deuxième print : ", data)
        return data
   
    
    def search_product(self):
        """"""
        categories = categorie()
        categories = categorie.objects.all()
        categorie_name = [categ.name for categ in categories]
        #print("Premier print :", categorie_name)
        for cat in categorie_name:
            for value in self.request_product(cat):
                new_values = op_food(id_categorie=categories.get(pk=cat), \
                name=value[0], nutriscore=value[1], ingredient=value[2], \
                picture_100g=value[3], picture=value[4], url=value[5])
                print("Troisième print : ", new_values)
                new_values.save()


    def handle(self, *args, **options):

        self.categorie_db()
        self.search_product()

