# Generated by Django 2.1.3 on 2018-11-24 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0002_task_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='slug',
            new_name='slug1',
        ),
    ]
