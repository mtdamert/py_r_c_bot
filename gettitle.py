import urllib.request


def getPageTitle(url):
    try:
        site = urllib.request.urlopen(url)
        siteStr = site.read().decode('utf-8')
        title = siteStr.split('<title>')[1].split('</title>')[0]
        return title
    except:
        print(f'URL title lookup failed for {url}')
