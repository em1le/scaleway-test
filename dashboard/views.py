from typing import Dict, Any

from django.db.models import QuerySet
from django.views.generic import ListView

from article.models import Article


class DashboardView(ListView):
    model = Article
    template_name = "dashboard/dashboard.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        return self.request.user.article_set.order_by('-created')

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
