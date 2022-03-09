import unittest
from app import app

class AmyDogTest(unittest.TestCase):

    def testBreeds_200(self):
        response = app.test_client().get('/breeds')
        self.assertEqual(200, response.status_code)

    def testBreedsByName_200(self):
        params = {'breed_name': 'boston'}
        response = app.test_client().get('/breedsbyname', query_string=params)
        self.assertEqual(200, response.status_code)



    def testBreedsByName_400(self):
        params = {'breed_name': ''}
        response = app.test_client().get('/breedsbyname', query_string=params)
        self.assertEqual(400, response.status_code)

    def testBreedImage_200(self):
        params = {'breed_id': 53 }
        response = app.test_client().get('/breedimage', query_string=params)
        self.assertEqual(200, response.status_code)

    def testBreedImage_400(self):
        params = {'breed_id': ''}
        response = app.test_client().get('/breedimage', query_string=params)
        self.assertEqual(400, response.status_code)



if __name__ == '__main__':
    unittest.main()
