from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
# Create your views here.


def home(request):
  if 'city' in request.POST:
    city = request.POST['city']
  else:
    city='Dhaka'
  appid = 'b5dbb987bbf24a4440c467a7b21c82dc'
  URL = 'https://api.openweathermap.org/data/2.5/weather'
  PARAMS = {'q':city,'appid':appid, 'units':'metric'}
  r = requests.get(url = URL ,params = PARAMS )
  res = r.json()
  description = res['weather'][0]['description']
  icon = res['weather'][0]['icon']
  temp = res['main']['temp']
  day = datetime.date.today()
  
  context = {'description':description, 'icon': icon,'temp': temp, 'title':'Weather','day':day,'city':city}
  return render(request, 'weatherapp/index.html',context)