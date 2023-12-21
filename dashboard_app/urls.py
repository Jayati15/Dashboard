# dashboard_app/urls.py
from django.urls import path
from .views import dashboard, update_preferences

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('update_preferences/', update_preferences, name='update_preferences'),
]
