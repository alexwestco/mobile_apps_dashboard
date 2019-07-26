from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import *


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        # User goes to home page
        request = self.factory.get("/")
        request.user = AnonymousUser()

        # Test if the home page responds correctly
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_seed_database(self):
        # Seed the database and check if it redirects us to the dashboard
        request = self.factory.get("/seed_database")
        request.user = AnonymousUser()

        # Check if it redirects us to the dashboard
        response = seed_database(request)
        self.assertEqual(response.status_code, 302)

    def test_dashboard(self):
        # Seed the database and check if it redirects us to the dashboard
        request = self.factory.get("/dashboard")
        request.user = AnonymousUser()

        # Check if it redirects us to the dashboard
        response = dashboard(request)
        self.assertEqual(response.status_code, 200)