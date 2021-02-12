from django.db import models

# Create your models here.


class WorkSheet(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    file_url = models.URLField(max_length=2083)
    file = models.FileField()


