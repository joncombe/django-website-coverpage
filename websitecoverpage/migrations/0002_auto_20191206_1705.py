# Generated by Django 2.1.8 on 2019-12-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitecoverpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitecoverpage',
            name='end_datetime',
            field=models.DateTimeField(verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='websitecoverpage',
            name='start_datetime',
            field=models.DateTimeField(verbose_name='Start time'),
        ),
    ]