from django.urls import include, path
from .views import EventDetailView, EventListView, EventCreateView, EventUpdateView, EventSignupView

urlpatterns = [
    path(
        'events',
        EventListView.as_view(),
        name='event_list'),
    path(
        'event/<int:event_id>',
        EventDetailView.as_view(),
        name='event_detail'),
    path(
        'event/add',
        EventCreateView.as_view(),
        name='event_add'),
    path(
        'event/<int:event_id>/edit',
        EventUpdateView.as_view(),
        name='event_edit'),
    path(
        'event/<int:event_id>/signup',
        EventSignupView.as_view(),
        name='event_signup'),
]

app_name = 'localevents'
