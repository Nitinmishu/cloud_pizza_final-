# Generated by Django 3.2.9 on 2021-12-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzap', '0004_auto_20211215_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_ordered',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.CharField(max_length=100),
        ),
    ]