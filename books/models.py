from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=128)
