from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_nickname = "Gabs",
            user_name = "Gabriele",
            user_email = "gabs@teste.com",
            user_age = 33
        )
        
    def test_get_all_users(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user_nickname'], "Gabs")
        
    def test_create_user(self):
        
        data = {
            "user_nickname": "Gabi3",
            "user_name": "Gabriele",
            "user_email": "gabi3@teste.com",
            "user_age": 30
        }
        
        response = self.client.post('/api/data/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        
    def test_update_user(self):
        data = {
            "user_nickname": "Gabs",
            "user_name": "Gabriele Atualizada",
            "user_email": "gabs@teste.com",
            "user_age": 34
        }
        response = self.client.put('/api/data/', data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        self.user.refresh_from_db()  
        self.assertEqual(self.user.user_name, "Gabriele Atualizada")
        self.assertEqual(self.user.user_age, 34)

    def test_delete_user(self):
        data = {"user_nickname": "Gabs"}
        
        response = self.client.delete('/api/data/', data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(User.objects.count(), 0)