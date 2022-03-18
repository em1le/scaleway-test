from django.urls import path, include

from account.views import SignupView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignupView.as_view(), name="signup"),
]
