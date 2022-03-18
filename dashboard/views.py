from typing import Dict, Any

from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from article.models import Article
from hardware.models import Hardware


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


class CreateHardwareView(CreateView):
    model = Hardware
    template_name = "dashboard/add.html"
    success_url = reverse_lazy("list-article")
    fields = [
        "brand",
        "model",
        "serial_number"
    ]


class CreateArticleView(CreateView):
    model = Article
    template_name = "dashboard/add.html"
    success_url = reverse_lazy("list-article")

    fields = [
        "quantity",
        "price",
        "hardware"
    ]

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteArticleView(DeleteView):
    model = Article
    template_name = "dashboard/delete.html"
    success_url = reverse_lazy("list-article")
