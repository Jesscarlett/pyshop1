from django.db import models

# Create your models here.


class Sheet(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    file_url = models.URLField(max_length=2083, blank=True, default='')
    file = models.FileField()

    class Meta:
        ordering = ('name',)

