# Generated by Django 4.1.3 on 2022-11-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_banner_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_subtitle',
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_placeholder',
            field=models.CharField(default='', max_length=300, verbose_name='search placeholder '),
        ),
    ]
