from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        # Cria um usuário e um token para autenticação
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_tasks(self):
        url = reverse('task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
