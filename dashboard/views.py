from typing import Dict, Any, Mapping

from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from article.models import Article
from hardware.models import Hardware


class DashboardView(ListView):
    model = Article
    template_name = "dashboard/dashboard.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        return self.request.user.article_set.order_by('-created')

    def get_context_data(self, **kwargs: Mapping) -> Dict[str, Any]:
        """Add more context to dashboard as we want to display disks listing."""
        context = super().get_context_data(**kwargs)
        models = set(Hardware.objects.values_list('model', flat=True))
        context["models"] = {model: Hardware.objects.listing_by_model(model, self.request.user) for model in models}
        inventory = Article.objects.get_inventory(user=self.request.user)
        context["disk_quantity"] = inventory["disk_quantity"]
        context["disk_amount"] = inventory["disk_amount"]
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


class UpdateArticleView(UpdateView):
    model = Article
    template_name = "dashboard/update.html"
    success_url = reverse_lazy("list-article")

    fields = [
        "quantity",
        "price",
        "hardware"
    ]
