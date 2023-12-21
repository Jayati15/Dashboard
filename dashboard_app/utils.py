# dashboard_app/utils.py
import requests

def fetch_covid_data():
    covid_api_url = 'https://api.rootnet.in/covid19-in/stats/latest'
    response = requests.get(covid_api_url)
    data = response.json()
    return data
