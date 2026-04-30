from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'user', 'email_address', 'role')
    list_filter = ('role',)
    search_fields = ('display_name', 'email_address', 'user__username')
