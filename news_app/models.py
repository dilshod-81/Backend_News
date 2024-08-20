from email import message
from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)