from decimal import Decimal
from random import randint, random

from factory import SubFactory
from factory.django import DjangoModelFactory

from account.factories import UserFactory
from hardware.factories import HardwareFactory
from article.models import Article


class ArticleFactory(DjangoModelFactory):

    class Meta:
        model = Article

    quantity = randint(1, 1000)
    price = Decimal(randint(1, 1000))
    hardware = SubFactory(HardwareFactory)
    user = SubFactory(UserFactory)
