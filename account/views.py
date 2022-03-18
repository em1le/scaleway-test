from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from account.forms import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        login(self.request, user=self.object)
        return HttpResponseRedirect(self.get_success_url())
