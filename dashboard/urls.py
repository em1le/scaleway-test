from django.contrib.auth.decorators import login_required
from django.urls import path

from dashboard.views import DashboardView, CreateHardwareView, CreateArticleView, DeleteArticleView, UpdateArticleView

urlpatterns = [
    path("", login_required(DashboardView.as_view()), name="list-article"),
    path("add/hardware/", login_required(CreateHardwareView.as_view()), name="add-hardware"),
    path("add/", login_required(CreateArticleView.as_view()), name="add-article"),
    path("delete/<int:pk>/", login_required(DeleteArticleView.as_view()), name="delete-article"),
    path("update/<int:pk>/", login_required(UpdateArticleView.as_view()), name="update-article")
]
