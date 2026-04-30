from functools import wraps

from django.shortcuts import redirect
from django.urls import reverse


def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                login_url = reverse('login')
                return redirect(f'{login_url}?next={request.path}')

            profile = getattr(request.user, 'profile', None)
            if profile is None or profile.role != required_role:
                return redirect(reverse('accounts:permission_denied'))

            return view_func(request, *args, **kwargs)

        return wrapped

    return decorator
