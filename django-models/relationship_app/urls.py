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

