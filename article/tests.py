from django.test import TestCase

from account.factories import UserFactory
from article.factories import ArticleFactory
from article.models import Article


class ArticleTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.article = ArticleFactory(user=cls.user)
        super().setUpTestData()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_total_price(self):
        expected = self.article.price * self.article.quantity
        result = self.article.total_price
        self.assertEqual(result, expected)

    def test_get_inventory(self):
        article2 = ArticleFactory(user=self.user)
        article3 = ArticleFactory(user=self.user)
        expected = {"disk_quantity": 0, "disk_amount": 0}
        for article in self.article, article2, article3:
            expected["disk_quantity"] += article.quantity
            expected["disk_amount"] += article.total_price
        result = Article.objects.get_inventory(user=self.user)
        self.assertDictEqual(result, expected)
