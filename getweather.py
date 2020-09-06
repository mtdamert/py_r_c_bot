import urllib.request
import json

# TODO make an object mapping cities to their lat and lon so that city names can be typed in instead
# locationDict = { "LA": { "lat": 0, "lon": 0}}


locationDict = {
    "ny": {
        "lat": 40,
        "lon": -73
    },
}


def loadLocations():
    loc_file = open("locs.txt", "r")
    for line in loc_file:
        ln = line.strip('\n\r')
        print(ln)
        splitLine = ln.split(", ")
        city = splitLine[0]
        lat = float(splitLine[1])
        lon = float(splitLine[2])
        locationDict[city] = {
            "lat": lat,
            "lon": lon,
        }
    print(locationDict)
    loc_file.close()


loadLocations()


def saveLocations():
    loc_file = open("locs.txt", "w+")
    loc_file.close()
    loc_file = open("locs.txt", "a+")
    for loc in locationDict:
        lat = locationDict[loc]['lat']
        lon = locationDict[loc]['lon']
        loc_file.write(f"{loc}, {lat}, {lon}\n")
    loc_file.close()


def addLocation(city, lat, lon):
    locationDict[city] = {
        "lat": lat,
        "lon": lon
    }
    saveLocations()


def printweather(lat, lon):
    # ...with TODO above. if lat in locationDict.keys(): locationDict[lat] etc...
    # rename lat to latOrCity?
    if (lat in locationDict):
        print(f"found location {lat} in locationDict, using stored vals")
        lon = locationDict[lat]["lon"]
        lat = locationDict[lat]["lat"]

    try:
        data = urllib.request.urlopen(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,daily,minutely&units=imperial&appid=4ba6a408966bcec7ac3ae7026c9ab365")
        wData = json.loads(data.read())
        # print(readableData) #prints very poorly
        # below is human readable
        # print(json.dumps(wData, indent=4, sort_keys=True))
        c = (wData['current']['temp']-32)/1.8
        c = format(c, ',.2f')
        cFeels = (wData['current']['feels_like']-32)/1.8
        cFeels = format(cFeels, ',.2f')
        return f"{wData['current']['temp']} fahrenheit ({c}c). {wData['current']['humidity']}% humidity. Feels like {wData['current']['feels_like']} fahrenheit ({cFeels}c). Generally: {wData['current']['weather'][0]['description']}."
    except:
        return "Something went wrong. Invalid location?"

# Old weather:

# import urllib.request
# import xml.etree.ElementTree as ET
# import pgeocode

# def printweather(zip_code):
#   zip_code = zip_code.strip()

#   if zip_code is None or zip_code == "":
#     return "But where? Please add a zip code after the weather command"

#   nomi = pgeocode.Nominatim('us')
#   latitude = nomi.query_postal_code(zip_code).latitude
#   latitude = str(latitude)
#   longitude = nomi.query_postal_code(zip_code).longitude
#   longitude = str(longitude)

#   # todo: get proper url for this user
#   site = urllib.request.urlopen("https://forecast.weather.gov/MapClick.php?lat=" + latitude + "&lon=" + longitude + "&unit=0&lg=english&FcstType=dwml")
#   site_source = site.read()
#   xml_root = ET.fromstring(site_source)

#   weather_location = xml_root.find("./head/source/production-center")
#   fahrenheit = xml_root.find("./data[@type='current observations']/parameters/temperature[@units='Fahrenheit']/value")
#   conditions = xml_root.find("./data[@type='current observations']/parameters/weather/weather-conditions[@weather-summary]")
#   return ("Current weather in " + weather_location.text + ": " + fahrenheit.text + "F, " + conditions.attrib['weather-summary'])
