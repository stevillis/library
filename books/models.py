from uuid import uuid4

from django.db import models


def upload_image_book(instance, filename):
    """Define image file name"""
    return f'{instance.id_book}-{filename}'


class Book(models.Model):
    """Book Model"""
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_book, null=True, blank=True)
