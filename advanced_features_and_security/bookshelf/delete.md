from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm the deletion by retrieving all books
Book.objects.all()
