# dashboard_app/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import SalesData
from .utils import fetch_api_data

class DashboardViewTest(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.sales_data = SalesData.objects.create(date='2023-01-01', revenue=1000)

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_uses_correct_template(self):
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_dashboard_view_contains_sales_data(self):
        response = self.client.get(reverse('dashboard'))
        self.assertIn(self.sales_data.date, str(response.content))
        self.assertIn(str(self.sales_data.revenue), str(response.content))

class UtilsTest(TestCase):
    def test_fetch_api_data(self):
        # Mock the API response for testing
        expected_data = {'key': 'value'}
        self.assertEqual(fetch_api_data(), expected_data)
