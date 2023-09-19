from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Task 1', 'description': 'Description of Task 1'}
        self.task = Task.objects.create(title='Task 2', description='Description of Task 2')

    def test_create_task(self):
        response = self.client.post('/tasklist', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_task_empty_data(self):
        response = self.client.post('/tasklist', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_task_list(self):
        response = self.client.get('/tasklist')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['Success']), 1)

    def test_retrieve_task_detail(self):
        response = self.client.get(f'/tasklist/{self.task.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(f'/tasklist/{self.task.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        response = self.client.delete(f'/tasklist/{self.task.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_get_nonexistent_task(self):
        response = self.client.get('/tasklist/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_nonexistent_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put('/tasklist/999', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_task(self):
        response = self.client.delete('/tasklist/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
