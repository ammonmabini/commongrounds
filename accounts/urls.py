from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('permission-denied/', views.permission_denied, name='permission_denied'),
    path('<str:username>', views.ProfileUpdateView.as_view(), name='profile_update'),
]
