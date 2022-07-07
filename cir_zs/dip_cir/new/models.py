from django.db import models
from django.urls import reverse


# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='new/images/')
    url = models.URLField(blank=True)
    date_new = models.DateField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date_new']