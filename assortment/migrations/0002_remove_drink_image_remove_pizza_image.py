# Generated by Django 4.0.3 on 2022-03-05 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assortment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='image',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='image',
        ),
    ]