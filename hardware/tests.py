from django.test import TestCase

from hardware.models import Hardware
from article.factories import ArticleFactory


class HardwareTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.article = ArticleFactory()
        super().setUpTestData()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_listing_by_model(self):
        expected = {"quantity": self.article.quantity, "price": self.article.price}
        hardware_model = self.article.hardware.model
        result = Hardware.objects.listing_by_model(hardware_model, self.article.user)
        self.assertDictEqual(result, expected)
