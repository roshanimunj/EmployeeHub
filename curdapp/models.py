from django.db import models

# Create your models here.
class Employess (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=50)
    phone = models.IntegerField(max_length=50)


    def __str__(self):
        return self.name





