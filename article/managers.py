from decimal import Decimal
from typing import Dict

from django.db import models


class ArticleManager(models.Manager):

    def get_inventory(self, user) -> Dict[str, Decimal | int]:
        inventory = {"disk_quantity": 0, "disk_amount": 0}
        for article in self.filter(user=user):
            inventory["disk_quantity"] += article.quantity
            inventory["disk_amount"] += article.total_price
        return inventory

