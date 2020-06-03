import urllib.request
import xml.etree.ElementTree as ET

def printweather():
  # todo: get proper url for this user
  site = urllib.request.urlopen("https://forecast.weather.gov/MapClick.php?lat=40.1051&lon=-75.1502&unit=0&lg=english&FcstType=dwml")
  str = site.read()
  xml_root = ET.fromstring(str)

  weather_location = xml_root.find("./head/source/production-center")
  fahrenheit = xml_root.find("./data[@type='current observations']/parameters/temperature[@units='Fahrenheit']/value")
  conditions = xml_root.find("./data[@type='current observations']/parameters/weather/weather-conditions[@weather-summary]")
  return ("Current weather in " + weather_location.text + ": " + fahrenheit.text + "F, " + conditions.attrib['weather-summary'])

#test
#printweather()
