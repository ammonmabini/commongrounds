from django import forms

from .models import Event


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'category',
            'event_image',
            'description',
            'location',
            'start_time',
            'end_time',
            'event_capacity',
            'status',
        ]


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'category',
            'event_image',
            'description',
            'location',
            'start_time',
            'end_time',
            'event_capacity',
            'status',
        ]


class GuestEventSignupForm(forms.Form):
    new_registrant = forms.CharField(
        max_length=255,
        label='Name',
        widget=forms.TextInput(attrs={'autocomplete': 'name'}),
    )
