from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import ProfileUpdateForm, RegisterForm
from .models import Profile


def home(request):
    if request.user.is_authenticated and request.session.get('pending_purchase'):
        return redirect('merchstore:complete_pending_purchase')

    return render(request, 'accounts/home.html')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.session.get('pending_purchase'):
                return redirect('merchstore:complete_pending_purchase')
            return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})


def permission_denied(request):
    return render(request, 'accounts/permission_denied.html', status=403)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_object_or_404(
            Profile,
            user__username=self.kwargs.get('username'),
            user=self.request.user,
        )
