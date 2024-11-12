from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
import json
from datetime import datetime, timezone

"""
    This is basic django web application. In this web app we are fetching the weather data from api and use the data to show the weather details.

"""
def home(request):
    # API Key
    key = "YOUR API KEY"
    if 'city' in request.POST:
        city = request.POST['city'].capitalize()
    else:
        city = 'Gurgaon'
    try:
        # API to fetch the weather report
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
     
        params = {
            'units':'metric'
        }
        
        response = requests.get(url, params =params).json()
        
        temp = response['main']['temp']
        icon = response['weather'][0]['icon']
        
        date = datetime.fromtimestamp(response['dt'], tz=timezone.utc).strftime('%d-%m-%Y')
        
        return render(request, 'weatherapp/index.html',{'icon':icon,'temp':temp,'date':date,'city':city,'exception_occured': False})
    except:
        messages.error(request, 'entered data is not available to api')
        return render(request, 'weatherapp/index.html',{'icon':'NA','temp':'NA','city':'NA','exception_occured': True} )


