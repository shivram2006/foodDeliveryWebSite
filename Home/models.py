
from django.db import models

# Create your models here.
# class Services(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     description = models.TextField()

class FormSubmit(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    description = models.TextField()