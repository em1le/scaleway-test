from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseLogModel(models.Model):
    """Represents a base log model which have logging attributes"""

    created = models.DateTimeField(
        verbose_name=_("Date de création"),
        auto_now_add=True
    )

    modified = models.DateTimeField(
        verbose_name=_("Date de modification"),
        auto_now=True
    )

    class Meta:
        abstract = True
