from django.db import models
import datetime

# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    date_uploaded = models.DateField(default=datetime.datetime.now)
    file = models.FileField(upload_to='files',null=True,blank=True)
    number_of_emails = models.IntegerField(default=0)
    number_of_downloads = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title 