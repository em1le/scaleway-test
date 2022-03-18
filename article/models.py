from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseLogModel
from article.managers import ArticleManager


class Article(BaseLogModel):

    quantity = models.PositiveSmallIntegerField(verbose_name=_("Quantité"))

    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_("Prix"))

    hardware = models.ForeignKey(
        to="hardware.Hardware", on_delete=models.DO_NOTHING, verbose_name=_("Matériel")
    )

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name=_("Utilisateur")
    )

    objects = ArticleManager()

    def __str__(self) -> str:
        return f"{self.hardware}"

    @property
    def total_price(self) -> Decimal:
        return self.price * self.quantity
