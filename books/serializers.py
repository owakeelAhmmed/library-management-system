from rest_framework import serializers
from .models import Book, Author




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # ['id', 'name', 'biography']

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        
        # ['id', 'title', 'author']


    # def create(self, validated_data):
    #     author_data = validated_data.pop('author')
    #     author = Author.objects.create(**author_data)
    #     book = Book.objects.create(author=author, **validated_data)
    #     return book