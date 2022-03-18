from decimal import Decimal
from typing import Dict

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class HardwareManager(models.Manager):
    def listing_by_model(self, model: str, user: User) -> Dict[str, Decimal | int]:
        return self.filter(model=model, article__user=user).aggregate(
            quantity=Sum("article__quantity", default=0),
            price=Sum("article__price", default=0),
        )
