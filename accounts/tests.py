from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class AccountsTests(TestCase):
    def test_register_creates_profile_with_selected_role(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'seller',
            'display_name': 'Market Seller',
            'email_address': 'seller@example.com',
            'role': Profile.ROLE_MARKET_SELLER,
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123',
        })

        self.assertRedirects(response, reverse('home'))
        user = User.objects.get(username='seller')
        self.assertEqual(user.profile.display_name, 'Market Seller')
        self.assertEqual(user.profile.email_address, 'seller@example.com')
        self.assertEqual(user.profile.role, Profile.ROLE_MARKET_SELLER)

    def test_profile_update_changes_display_name_only(self):
        user = User.objects.create_user(
            username='buyer',
            password='StrongPassword123',
        )
        user.profile.email_address = 'buyer@example.com'
        user.profile.save()
        self.client.force_login(user)

        response = self.client.post(
            reverse('accounts:profile_update', kwargs={'username': user.username}),
            {
                'display_name': 'Updated Buyer',
                'email_address': 'changed@example.com',
            },
        )

        self.assertRedirects(response, reverse('home'))
        user.profile.refresh_from_db()
        self.assertEqual(user.profile.display_name, 'Updated Buyer')
        self.assertEqual(user.profile.email_address, 'buyer@example.com')
