# Generated by Django 2.1.3 on 2018-11-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]