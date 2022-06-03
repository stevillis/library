from dataclasses import fields
from rest_framework import serializers
from books import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'