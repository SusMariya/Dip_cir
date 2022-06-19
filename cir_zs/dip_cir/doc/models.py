from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    r_doc = models.FileField()

    def __str__(self):
        return self.title

    def is_valid(self):
        pass