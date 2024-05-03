# models.py
from django.db import models

class ConverterUploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
