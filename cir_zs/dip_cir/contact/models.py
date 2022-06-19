from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name="ФИО должность")
    content = models.TextField(blank=True, verbose_name="Контент")
    c_adres = models.TextField(blank=True, verbose_name="Адрес")
    c_mail = models.EmailField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title