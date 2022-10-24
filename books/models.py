from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    name_full = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre', related_name='book')
    cover = models.FileField(upload_to='img/')
    anotation = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

