# dashboard_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from .models import SalesData, UserPreferences
from .utils import fetch_covid_data

@cache_page(60 * 15)  # Cache for 15 minutes
@login_required
def dashboard(request):
    user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)
    sales_data = SalesData.objects.all()

    if not user_preferences.show_api_data:
        api_data = None
    else:
        api_data = fetch_covid_data()
    
    # Filtering based on user preferences
    if user_preferences.filter_by_date:
        sales_data = sales_data.filter(date__gte=user_preferences.start_date, date__lte=user_preferences.end_date)
    
    # Sorting based on user preferences
    if user_preferences.sort_by_revenue:
        sales_data = sales_data.order_by('-revenue')
    
    return render(request, 'dashboard.html', {'sales_data': sales_data, 'api_data': api_data, 'user_preferences': user_preferences})

@login_required
def update_preferences(request):
    if request.method == 'POST':
        user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)
        user_preferences.show_api_data = 'show_api_data' in request.POST
        user_preferences.filter_by_date = 'filter_by_date' in request.POST
        user_preferences.start_date = request.POST.get('start_date')
        user_preferences.end_date = request.POST.get('end_date')
        user_preferences.sort_by_revenue = 'sort_by_revenue' in request.POST
        user_preferences.save()
    
    return redirect('dashboard')

