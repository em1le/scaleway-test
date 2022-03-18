from django.contrib.auth.decorators import login_required
from django.urls import path

from dashboard.views import DashboardView


urlpatterns = [
    path("", login_required(DashboardView.as_view()), name="list-article")
]
