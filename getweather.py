import urllib.request
import json
import os #need this to get geocode api from dotenv file
from opencage.geocoder import OpenCageGeocode

geoCodeKey = os.environ.get("GEOCODE_KEY")

# TODO make an object mapping cities to their lat and lon so that city names can be typed in instead
# locationDict = { "LA": { "lat": 0, "lon": 0}}
# print(geoCodeKey)

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


def printweather(city):
    # check for city in saved locations
    lon = False
    lat = False
    if (city in locationDict):
        print(f"found location {city} in locationDict, using stored vals")
        lon = locationDict[city]["lon"]
        lat = locationDict[city]["lat"]
    # not in saved, use geocoding to find it using name, add and save
    else:
        try:
            print(f"{city} not found, using geocoding")
            geocoder = OpenCageGeocode(geoCodeKey)
            results = geocoder.geocode(f"{city}")
            print(f"RESULTS: ")
            print(f"LAT: {results[0]['geometry']['lat']}")
            print(f"LONG: {results[0]['geometry']['lng']}")
            lat = int(results[0]['geometry']['lat'])
            lon = int(results[0]['geometry']['lng'])
            if lat and lon:
                addLocation(city, lat, lon)
        except:
            return "Something went wrong. Invalid location?"

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
