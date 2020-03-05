from django.urls import reverse
from django.test import TestCase
from .views import index, log_out, log_in, sign_up

    
class IndexPageTestCase(TestCase):
    """test that index page returns a status code 200"""

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class loginPageTestCase(TestCase):
    """test that login page returns a status code 200"""
    def test_log_in_page(self):
        response = self.client.get(reverse('search:log_in'))
        self.assertEqual(response.status_code, 200)

class signup_PageTestCase(TestCase):
    """test that logout page returns a status code 200"""
    def test_sign_up_page(self):
        response = self.client.get(reverse('search:sign_up'))
        self.assertEqual(response.status_code, 200)
