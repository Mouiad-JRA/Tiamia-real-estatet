from wagtail.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"


class TextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    class Meta:
        template = "streams/text_block.html"
        icon = "edit"
        label = "Title & Text"
