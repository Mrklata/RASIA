from django.db import models


class Contact(models.Model):
    number = models.CharField(max_length=12, default=+48513294634)
    adress = models.CharField(max_length=100)


class Image(models.Model):
    SECTION = (
        ("logo", "logo"),
        ("href", "odnośnik"),
        ("image", "zdjęcie")
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    section = models.CharField(max_length=100, choices=SECTION)

# Create your models here.
