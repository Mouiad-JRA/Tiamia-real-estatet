from django.db import models
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page


class HomePage(Page):
    templates = "home/home_page.html"
    max_count = 1
    banner_title = models.CharField(_("banner title "), max_length=300, default="")

    content_panels = Page.content_panels + [FieldPanel('banner_title'),]


    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
