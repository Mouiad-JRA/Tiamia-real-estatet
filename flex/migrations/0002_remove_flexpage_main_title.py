# Generated by Django 4.1.3 on 2022-11-21 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='main_title',
        ),
    ]
