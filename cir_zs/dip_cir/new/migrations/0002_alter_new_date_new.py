# Generated by Django 4.0.4 on 2022-06-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date_new',
            field=models.DateField(),
        ),
    ]