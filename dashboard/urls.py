from django.contrib.auth.decorators import login_required
from django.urls import path

from dashboard.views import DashboardView, CreateHardwareView, CreateArticleView

urlpatterns = [
    path("", login_required(DashboardView.as_view()), name="list-article"),
    path("add/", login_required(CreateArticleView.as_view()), name="add-article"),
    path("add/hardware/", login_required(CreateHardwareView.as_view()), name="add-hardware")
]
