from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Author
from .serializers import AuthorSerializer
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly, IsMember


class BookViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Get details of a specific book.

    list:
    Get a list of all books.

    create:
    Add a new book (Admin only).

    update:
    Update book details (Admin only).

    partial_update:
    Partially update book details (Admin only).

    destroy:
    Delete a book (Admin only).

    borrow:
    Borrow a book (Members only).

    return_book:
    Return a borrowed book (Members only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsMember])
    def borrow(self, request, pk=None):
        book = self.get_object()
        if book.available_copies > 0:
            book.available_copies -= 1
            book.save()
            return Response({"message": f"You borrowed '{book.title}' successfully"})
        return Response({"message": "No copies available"}, status=400)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsMember])
    def return_book(self, request, pk=None):
        book = self.get_object()
        book.available_copies += 1
        book.save()
        return Response({"message": f"You returned '{book.title}' successfully"})
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
