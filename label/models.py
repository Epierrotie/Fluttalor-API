from django.db import models
from django.contrib.auth.models import User
# from contact.models import Contact

# Create your models here.
class Label(models.Model):
    name = models.CharField("name", max_length=45)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name