from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    url = models.URLField(blank=True)
