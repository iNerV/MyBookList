from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.http import Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.core.exceptions import PermissionDenied
from braces.views import LoginRequiredMixin
from accounts.models import User


class UsersList(ListView):
    model = User
    template_name = 'accounts/user_list.html'
    paginate_by = 10


class UserDetail(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'


class UserSettings(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/user_settings.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'city', 'about']

    def get_object(self, queryset=None):
        user = super(UserSettings, self).get_object()
        if user != self.request.user:
            raise PermissionDenied
        return user
