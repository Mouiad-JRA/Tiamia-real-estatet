from django.db import models

# Create your models here.
from wagtail.admin.panels import FieldPanel
from wagtail.core.models import Page
from wagtail.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from wagtail.images.edit_handlers import ImageChooserPanel


class FlexPage(Page):
    """
    Flexible page class
    """

    templates = "home/flex_page.html"

    sub_title_one = RichTextField(_(" Sub title one"))
    sub_title_two = RichTextField(_(" Sub title two"))
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels + [
        FieldPanel('sub_title_one'),
        FieldPanel('sub_title_two'),
        ImageChooserPanel('banner_image'),

    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
