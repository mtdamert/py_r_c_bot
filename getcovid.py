import urllib.request
import json


def withCommas(num):
    return format(int(num), ',')


def getCovidData(reqObj):
    if reqObj["type"] == "zip":
        try:
            zipcode = reqObj["code"]
            data = urllib.request.urlopen(
                f"https://localcoviddata.com/covid19/v1/cases/newYorkTimes?zipCode={zipcode}&daysInPast=5")
            cData = json.loads(data.read())
            # print(json.dumps(cData, indent=4, sort_keys=True))
            days = cData["counties"][0]["historicData"]
            county = cData["counties"][0]["countyName"]
            returnStr = f"{county}, date/dead/infected: "
            for day in days:
                returnStr += f"{day['date']} / {withCommas(day['deathCt'])} / {withCommas(day['positiveCt'])} ||| "
            return returnStr
        except:
            return "Something went wrong with the zipcode."
    elif reqObj["type"] == "countrycode":
        print(reqObj['code'])
        try:
            data = urllib.request.urlopen(
                f"https://covid19-api.org/api/timeline/{reqObj['code']}")
            cData = json.loads(data.read())
            # print(json.dumps(cData, indent=4, sort_keys=True))
            countryName = cData[0]["country"]

            days = []
            for i in range(5):
                days.append(cData[i])

            returnStr = f"{countryName}, date/dead/infected: "
            for day in days:
                day['last_update'] = day['last_update'].split('-')
                day['last_update'].pop(0)
                day['last_update'] = '-'.join(day['last_update'])
                day['last_update'] = day['last_update'].split('T')[0]
                returnStr += f"{day['last_update']} / {withCommas(day['deaths'])} / {withCommas(day['cases'])} ||| "
            return returnStr
        except:
            return "Something went wrong with the country code."
    else:
        return "Neither zip nor countrycode found."
