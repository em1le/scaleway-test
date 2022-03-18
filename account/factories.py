from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from factory.faker import Faker


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = Faker("user_name")
