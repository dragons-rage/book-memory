from bookorganizer.models import Book


def run():
    books = Book.objects.all()
    books.delete()
