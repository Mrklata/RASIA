from django.db import models


class Contact(models.Model):
    number = models.CharField(max_length=12, default=+48513294634)
    adress = models.CharField(max_length=100)


class Image(models.Model):
    SECTION = (
        ("bathroom", "łazienka"),
        ("kitchen", "kuchnia"),
        ("closet", "szafy"),
        ("beds", "łóżka"),
        ("other", "inne"),
        ("back", "zaplecze"),
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000, default="Ah ta jakość")
    image = models.ImageField(upload_to='media')
    section = models.CharField(max_length=100, choices=SECTION)

# Create your models here.
