# dashboard_app/models.py
from django.db import models
from django.contrib.auth.models import User

class SalesData(models.Model):
    date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_api_data = models.BooleanField(default=True)
    filter_by_date = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    sort_by_revenue = models.BooleanField(default=False)
    # Add other preferences as needed
