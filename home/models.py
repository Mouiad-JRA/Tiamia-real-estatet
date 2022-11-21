from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from django.utils.translation import gettext_lazy as _
from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page


class HomePage(Page):
    templates = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(
        _("banner subtitle "), max_length=300, default="")
    search_placeholder = models.CharField(
        _("search placeholder "), max_length=300, default="")
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('search_placeholder'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta'),

    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
