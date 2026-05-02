from django.conf import settings
from django.db import migrations


def create_missing_profiles(apps, schema_editor):
    user_app_label, user_model_name = settings.AUTH_USER_MODEL.split('.')
    User = apps.get_model(user_app_label, user_model_name)
    Profile = apps.get_model('accounts', 'Profile')

    for user in User.objects.all():
        Profile.objects.get_or_create(
            user=user,
            defaults={
                'display_name': user.username,
                'email_address': user.email,
                'role': 'Member',
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_missing_profiles, migrations.RunPython.noop),
    ]
