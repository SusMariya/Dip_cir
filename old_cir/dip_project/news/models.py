from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='news/images/')
    url = models.URLField(blank=True)
    date_new = models.DateField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title