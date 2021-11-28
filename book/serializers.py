from .models import Book
from rest_framework import serializers

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'volume', 'author', 'total_page', 'publisher', 'published_date']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author']

