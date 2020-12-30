from django.db import models
from django.contrib.auth.models import User
from label.models import Label

# Create your models here.
class Contact(models.Model):
    nickname = models.CharField("nickname", max_length=45, blank=True, default="")
    firstname = models.CharField("firstname", max_length=45, blank=True, default="")
    lastname = models.CharField("lastname", max_length=45, blank=True, default="")

    email = models.EmailField("email", max_length=255, blank=True, default="")
    phone = models.CharField("phone", max_length=255, blank=True, default="")
    address = models.CharField("address", max_length=255, blank=True, default="")

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    icon = models.ImageField(upload_to='contact', null=True, blank=True)

    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        name = self.nickname
        if name == "":
            name = self.firstname
        if name == "":
            name = self.lastname
        if name == "":
            name = self.pk

        return name