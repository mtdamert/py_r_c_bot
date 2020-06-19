import urllib.request
import xml.etree.ElementTree as ET
import pgeocode

def printweather(zip_code):
  zip_code = zip_code.strip()

  if zip_code is None or zip_code == "":
    return "But where? Please add a zip code after the weather command"

  nomi = pgeocode.Nominatim('us')
  latitude = nomi.query_postal_code(zip_code).latitude
  latitude = str(latitude)
  longitude = nomi.query_postal_code(zip_code).longitude
  longitude = str(longitude)

  # todo: get proper url for this user
  site = urllib.request.urlopen("https://forecast.weather.gov/MapClick.php?lat=" + latitude + "&lon=" + longitude + "&unit=0&lg=english&FcstType=dwml")
  site_source = site.read()
  xml_root = ET.fromstring(site_source)

  weather_location = xml_root.find("./head/source/production-center")
  fahrenheit = xml_root.find("./data[@type='current observations']/parameters/temperature[@units='Fahrenheit']/value")
  conditions = xml_root.find("./data[@type='current observations']/parameters/weather/weather-conditions[@weather-summary]")
  return ("Current weather in " + weather_location.text + ": " + fahrenheit.text + "F, " + conditions.attrib['weather-summary'])

#test
#print(printweather())
