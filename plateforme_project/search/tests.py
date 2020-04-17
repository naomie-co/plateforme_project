from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from search.models import categorie, op_food

"""Tests views and the database models"""

class IndexPageTestCase(TestCase):
    """test that index page returns a status code 200"""
    def test_index_page(self): 
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class LogPagesTestCase(TestCase):

    def test_log_in_page(self):
        """test that login page returns a status code 200"""
        response = self.client.get(reverse('search:log_in'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_page(self):
        """test that sing_up page returns a status code 200"""
        response = self.client.get(reverse('search:sign_up'))
        self.assertEqual(response.status_code, 200)
    
    def test_log_out_page(self):
        """Test that logout page return a status code 200"""
        response = self.client.get(reverse('search:log_out'))
        self.assertEqual(response.status_code, 200)
    
class ProductsPagesTestCase(TestCase):
    """Tests products page and selection page"""
    
    def setUp(self):
        """Setup products in the models"""
        test_categorie = categorie.objects.create(name="taboulé")
        self.cat = categorie.objects.get(name="taboulé")
        test_product1 = op_food.objects.create(name="taboulé", nutriscore="d", \
        ingredient="test", nutritional_values="test", url="www.test.fr", \
        picture="", picture_100g="", categorie=self.cat)
        test_product2 = op_food.objects.create(name="taboulé2", nutriscore="c", \
        ingredient="test2", nutritional_values="test2", url="www.test2.fr", \
        picture="", picture_100g="", categorie=self.cat)
        self.product1 = op_food.objects.get(name="taboulé")
        self.product2 = op_food.objects.get(name="taboulé2")

    def test_detail_page_returns_200(self):
        """test that detail page returns a status code 200"""
        product_id = self.product1.id
        reponse = self.client.get(reverse('search:detail', args=(product_id,)))
        self.assertEqual(reponse.status_code, 200)

    def test_detail_page_returns_404(self):
        """test that detail page returns a status code 404 if the items does
        not exist"""
        product_id = self.product1.id + 2
        reponse = self.client.get(reverse('search:detail', args=(product_id,)))
        self.assertEqual(reponse.status_code, 404)

    def test_my_selection_authentificated(self):
        """Test that my_selection page returns a status code 303 to log_in page
        if the user is not authentificated"""
        user_test = {"user":234}
        reponse = self.client.get(reverse('search:my_selection', \
        args=(user_test)))
        self.assertEqual(reponse.status_code, 302)

    def test_products_page(self):
        """Test that if the user logs in, the product page is different from the u
        unconnected version"""

        page_without_log = self.client.get(reverse('search:products'))
        self.client.login(username="test_1", password="password")
        reponse = self.client.get(reverse('search:products'))
        #print(page_without_log)
        #print(reponse)
        self.assertNotEqual(reponse, page_without_log) 

class DataBaseTestCase(TestCase):
    """Test database models"""

    def setUp(self):
        """setup products in the models"""
        test_categorie = categorie.objects.create(name="taboulé")
        self.cat = categorie.objects.get(name="taboulé")
        test_product1 = op_food.objects.create(name="taboulé", nutriscore="d", \
        ingredient="test", nutritional_values="test", url="www.test.fr", \
        picture="", picture_100g="", categorie=self.cat)
        test_product2 = op_food.objects.create(name="taboulé2", \
        nutriscore="c", ingredient="test2", nutritional_values="test2", \
        url="www.test2.fr", picture="", picture_100g="", categorie=self.cat)
        self.product1 = op_food.objects.get(name="taboulé")
        self.product2 = op_food.objects.get(name="taboulé2")

    def test_user_create(self):
        """Test that a new user is created"""
        User.objects.create_user('user_test', 'user_test@test.com', \
        'testpassword')
        assert User.objects.count() == 1

    def test_op_food_table(self):
        """Test that a new obejct is created"""
        old_products = op_food.objects.count()
        op_food.objects.create(name="taboulé", nutriscore="d",\
        ingredient="test", nutritional_values="test", url="www.test.fr", \
        picture="", picture_100g="", categorie=self.cat)
        new_products = op_food.objects.count()
        self.assertEqual(new_products, old_products + 1)

    def test_categorie_table(self):
        """Test that a new categorie is created"""
        old_categorie = categorie.objects.count()
        categorie.objects.create(name="houmous")
        new_categorie = categorie.objects.count()
        self.assertEqual(new_categorie, old_categorie + 1)

