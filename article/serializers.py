from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ["user"]

    def create(self, validated_data):
        request = self.context["request"]
        article = Article.objects.create(user=request.user, **validated_data)
        return article
