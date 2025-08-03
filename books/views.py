from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer
