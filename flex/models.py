from django.db import models

# Create your models here.
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.fields import RichTextField, StreamField
from django.utils.translation import gettext_lazy as _
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class FlexPage(Page):
    """
    Flexible page class
    """

    templates = "home/flex_page.html"

    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
        ],
        blank=True, null=True
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels + [

        ImageChooserPanel('banner_image'),
        StreamFieldPanel('content'),

    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
