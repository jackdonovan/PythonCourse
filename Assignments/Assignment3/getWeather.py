import requests
import json
import geocoder

with open('license.txt', 'r') as licenseFile:
    idkey = licenseFile.read()


g = geocoder.ip('me')

lat = g.latlng[0]
lng = g.latlng[1]

weatherUrl = 'http://api.openweathermap.org/data/2.5/weather'
r = requests.get(url=weatherUrl, params=dict(APPID=idkey, lat = lat, lon = lng))
jdict = json.loads(r.text)

tempKelvin = float(jdict.get('main').get('temp'))
tempFahr = (tempKelvin-273.15) * (9/5) + 32
print("current location: lat: %f, long: %f" %(lat, lng))
print("The current temperature in your area is %.3f degrees Fahrenheit" % (tempFahr))