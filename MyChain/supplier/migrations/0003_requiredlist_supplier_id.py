# Generated by Django 3.1.1 on 2020-12-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_auto_20201201_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='requiredlist',
            name='supplier_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
