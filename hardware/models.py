from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseLogModel
from hardware.managers import HardwareManager


class Hardware(BaseLogModel):

    brand = models.CharField(
        verbose_name=_("Marque"),
        max_length=80
    )

    model = models.CharField(
        verbose_name=_("Modèle"),
        max_length=80
    )

    serial_number = models.CharField(
        verbose_name=_("Numéro de série"),
        max_length=100
    )

    objects = HardwareManager()

    def __str__(self) -> str:
        return f"{self.brand} - {self.model}"

    class Meta:
        verbose_name = _("Matériel")
        verbose_name_plural = _("Matériels")
