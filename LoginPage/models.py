from django.db import models

# Create your models here.
class RegistrationPage(models.Model):
    FirstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.TextField(max_length=12)
    password = models.CharField(max_length=12)
    birthDate = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    