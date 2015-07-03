from django.test import TestCase, LiveServerTestCase
#from handler.lazy_load import find_city
from django.test.client import Client
from tastypie.test import ResourceTestCase
import json

# URI = '/api/zip_table/'

# class InternalTest(TestCase):
#     fixtures = ['handler.json']
#     def test_cities_models_positive(self):
#         city_is = find_city('01279', 'Germany')
#         print city_is
#         self.assertEqual(city_is, u'Dresden')
        
#     def test_cities_models_wrong_data(self):
#         city = find_city('90210', 'Germany')
#         self.assertEqual(city, False)

class TastypieTest(ResourceTestCase):
    fixtures = ['handler.json']
    def setUp(self):
        super(TastypieTest, self).setUp()
        self.post_data = {'zip_code':'90210', 'country': 'United States'}
    
    def test_post_request_available(self):
        self.assertHttpOK(self.api_client.post('/api/zip_table/', format='json', data=self.post_data))

    def test_post_request_response_and_get_data(self):
        response = self.api_client.post('/api/zip_table/', format='json', data=self.post_data)
        self.assertJSONEqual(
            response.content,
            {"city": "Beverly Hills"}
        )

    def test_post_request_response_and_get_data_next(self):
        data = {'zip_code':'01279', 'country': 'Germany'}
        response = self.api_client.post('/api/zip_table/', format='json', data=data)
        self.assertJSONEqual(
            response.content,
            {"city": "Dresden"}
        )

    def test_post_request_response_wrong_data(self):
        data = {'zip_code':'90210', 'country': 'Germany'}
        response = self.api_client.post('/api/zip_table/', format='json', data=data)
        self.assertJSONEqual(
            response.content,
            {"error": "Country and zip code missmatch"}
        )




# Create your tests here.
