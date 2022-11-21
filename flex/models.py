from django.db import models

# Create your models here.
from wagtail.admin.panels import FieldPanel
from wagtail.core.models import Page
from wagtail.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class FlexPage(Page):
    """
    Flexible page class
    """

    templates = "home/flex_page.html"

    sub_title = RichTextField(_(" Sub title"))
    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),

    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
