from django.test import TestCase
from search.models import categorie, op_food


class InitDatabaseTestCase(TestCase):
    """test the API request and the filling of the database"""
    def test_request_product(self): 
    	"""Mock an API request with a tag in parameter.
        Store the result in a list of list named data"""
        @mock.patch('requests.get')
        def test_request_product(self, mock_get):
        	#define new Mock object
        	mock_response = mock.Mock()
        	#define response data from OFF API
        	expected_response = {

        	}

        	#define response data from my Mock object
        	mock_response.json.retunr_value = expected_response
        	mock_response.status_code = 200

        	#define response for the fake API
        	mock_get.return_value = mock_response

        	#call the function
        	result = test_resquest_product(self, query)

        	self.assertEqual(result, { })


        pass

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
        return data

    def test_search_product(self):
    	"""Mocks the category table, mocks a request to the OFF API. Tests if
    	the products have entered the op_food table"""
        pass