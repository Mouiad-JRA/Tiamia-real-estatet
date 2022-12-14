# Generated by Django 4.1.3 on 2022-11-21 17:55

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_options_homepage_banner_cta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_subtitle',
            field=models.CharField(default='', max_length=300, verbose_name='banner subtitle '),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_title',
            field=wagtail.fields.RichTextField(verbose_name='banner title '),
        ),
    ]
