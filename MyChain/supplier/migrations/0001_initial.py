# Generated by Django 3.1.1 on 2020-11-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requiredlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('Product_name', models.CharField(default='', max_length=50)),
                ('product_quantity', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
                ('product_quantity', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
