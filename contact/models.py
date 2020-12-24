from django.db import models
from django.contrib.auth.models import User
from label.models import Label

# Create your models here.
class Contact(models.Model):
    nickname = models.CharField("nickname", max_length=45, null=True, blank=True, default='')
    firstname = models.CharField("firstname", max_length=45, null=True, blank=True, default='')
    lastname = models.CharField("lastname", max_length=45, null=True, blank=True, default='')

    email = models.EmailField("email", max_length=255, null=True, blank=True, default='')
    phone = models.CharField("phone", max_length=255, null=True, blank=True, default='')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    icon = models.ImageField(upload_to='static/contact', null=True, blank=True)

    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        name = self.nickname
        if name is None:
            name = self.firstname
        if name is None:
            name = self.lastname

        return name