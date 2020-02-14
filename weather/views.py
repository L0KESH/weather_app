from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d98a83a75786da15c059b0716eedcfd7'
    # city = 'India'
    city = request.POST.get('text', 'London')
    # print(city)
    r = requests.get(url.format(city)).json()
    if r != "":
        # print(r.text)

        city_weather = {
            'city' : city,
            'temprature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        # print(city_weather)
        context = {'city_weather' : city_weather}
        return render(request, 'weather/weather.html', context)
    else:
        return HttpResponse("bye")