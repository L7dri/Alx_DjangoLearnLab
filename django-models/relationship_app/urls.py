from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', user_register, name='register'),
]
views.register

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add/', add_book/ , name='add_book'),
    path('edit/<int:pk>/', edit_book/ , name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
]
