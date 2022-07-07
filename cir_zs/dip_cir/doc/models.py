from django.db import models

# Create your models here.
class Doc(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    r_doc = models.FileField(upload_to='', blank=True, verbose_name='Файлы')
    # url = models.URLField(blank=True)
    def __str__(self):
            return self.title



# class DocsFiles(models.Model):
#     reg_doc = models.FileField(upload_to='uploads/', blank=True, verbose_name='Файлы')
#     r_doc = models.ForeignKey('Doc', on_delete=models.PROTECT)
#
#     def is_valid(self):
#         pass

    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = "Документы"


