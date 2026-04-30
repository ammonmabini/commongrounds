from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    display_name = forms.CharField(max_length=63)
    email_address = forms.EmailField()
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'display_name', 'email_address', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email_address')
        if commit:
            user.save()
            profile = user.profile
            profile.display_name = self.cleaned_data.get('display_name')
            profile.email_address = self.cleaned_data.get('email_address')
            profile.role = self.cleaned_data.get('role')
            profile.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('display_name',)
