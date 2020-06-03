import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
# my library
import getdate

def printskdtheme():
    site = urllib.request.urlopen("https://www.reddit.com/r/SketchDaily/")
    site_str = site.read().decode('utf-8')

    # search for today's theme on the skd site
    now = datetime.now()
    neat_today_date = getdate.getneattodaydate(now)
    loc = site_str.find(neat_today_date + " - ")

    # if we can't find today's theme, search for yesterday's theme
    if (loc == -1):
        now = datetime.now() - timedelta(days = 1)
        neat_today_date = getdate.getneattodaydate(now)
        loc = site_str.find(neat_today_date + " - ")

    # neither today's nor yesterday's theme found
    if loc == -1:
        return "Failed to locate latest SKD Theme. Sorry! :c"

    site_str = site_str[loc:]
    site_str = site_str[:site_str.find('<')]
    if len(site_str) > 100:
        site_str = site_str[:100]
    
    return site_str
