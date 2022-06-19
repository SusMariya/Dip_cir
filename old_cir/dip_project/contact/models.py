from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Контент")