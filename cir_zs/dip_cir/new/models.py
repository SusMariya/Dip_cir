from django.db import models


# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='new/images/')
    url = models.URLField(blank=True)
    date_new = models.DateField()

    def __str__(self):
        return self.title
