from django.db import models

# Create your models here.
class files(models.Model):
    file_name: str = models.CharField(max_length=100)
    file_size: str = models.CharField()
    file_bytes: str = models.EmailField()
