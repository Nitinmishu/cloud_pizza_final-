# Generated by Django 3.2.9 on 2021-12-15 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzap', '0003_auto_20211215_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='thumbnail',
        ),
    ]
