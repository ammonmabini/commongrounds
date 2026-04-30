from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse


class RoleRequiredMixin(LoginRequiredMixin):
    required_role = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        profile = getattr(request.user, 'profile', None)
        if self.required_role and (
            profile is None or profile.role != self.required_role
        ):
            return redirect(reverse('accounts:permission_denied'))

        return super().dispatch(request, *args, **kwargs)
