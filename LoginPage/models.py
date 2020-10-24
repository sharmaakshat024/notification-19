from django.db import models

# Create your models here.
class RegistrationPage(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField()
    Password = models.TextField(max_length=12)
    ConfirmPassword = models.CharField(max_length=12)
    DateOfBirth = models.EmailField()
    PhoneNumber = models.CharField(max_length=10)
    