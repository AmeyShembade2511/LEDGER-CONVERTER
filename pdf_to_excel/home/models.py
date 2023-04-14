from django.db import models
from django import forms
# Create your models here.
class FilesUpload(models.Model):
    file=models.FileField()