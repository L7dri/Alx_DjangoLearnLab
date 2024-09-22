from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create some test data
        self.book1 = Book.objects.create(title="Book One", author="Author One", published_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", published_year=2005)
        
        # Endpoint URLs
        self.list_create_url = reverse('book-list-create')  # assuming you named the url 'book-list-create'
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})  # 'book-detail'

    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'published_year': 2020}
        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_get_book_list(self):
        response = self.client.get(self.list_create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        update_data = {'title': 'Updated Book', 'author': 'Updated Author', 'published_year': 2020}
        response = self.client.put(self.detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        response = self.client.get(self.list_create_url, {'published_year': 2000}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_create_url, {'search': 'Author One'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        response = self.client.get(self.list_create_url, {'ordering': 'published_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['published_year'], 2000)
