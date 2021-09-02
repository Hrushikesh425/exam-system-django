from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return str(self.name)
    