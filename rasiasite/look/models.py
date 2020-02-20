from django.db import models


class Contact(models.Model):
    number = models.IntegerField(max_length=12, default=+48513294634)
    adres = models.CharField(max_length=100)


class File(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
# Create your models here.
