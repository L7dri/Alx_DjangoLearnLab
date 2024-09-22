from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
filters.SearchFilter
# ListView to retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# DetailView to retrieve a single book by its ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework.permissions import IsAuthenticated

# CreateView to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Apply permissions to the ListView and DetailView
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields to filter by

from rest_framework.filters import SearchFilter

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']  # Fields to search in
from rest_framework.filters import OrderingFilter

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']  # Fields to order by
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
filters.OrderingFilter
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields to filter by
    search_fields = ['title', 'author__name']  # Fields to search in
    ordering_fields = ['title', 'publication_year']  # Fields to order by
