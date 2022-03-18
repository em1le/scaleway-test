from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence
from hardware.models import Hardware


class HardwareFactory(DjangoModelFactory):

    class Meta:
        model = Hardware

    brand = Faker('company')
    model = Faker('company')
    serial_number = Sequence(lambda n: '00000000%d' % n)
