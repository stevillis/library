
from books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""
    class Meta:
        """Medata options"""
        model = Book
        fields = '__all__'
