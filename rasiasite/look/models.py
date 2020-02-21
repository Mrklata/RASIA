from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    # __str__ method
    # Meta

    # It is number field, how do you want to store '+' sign?
    number = models.IntegerField(default=+48513294634)
    adres = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.adres}: {self.number}"

    class Meta:
        verbose_name = "ZIEMNIAK"
        verbose_name_plural = _("ZIEMNIAKI")


class File(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    # It's always uploading to media folder, here you name the subfolder
    image = models.ImageField(upload_to='media')
# Create your models here.
