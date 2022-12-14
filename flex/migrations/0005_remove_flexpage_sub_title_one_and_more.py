# Generated by Django 4.1.3 on 2022-11-21 19:04

from django.db import migrations
import streams.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0004_remove_flexpage_sub_title_flexpage_sub_title_one_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='sub_title_one',
        ),
        migrations.RemoveField(
            model_name='flexpage',
            name='sub_title_two',
        ),
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('full_rich_text', streams.blocks.RichTextBlock())], blank=True, null=True, use_json_field=None),
        ),
    ]
