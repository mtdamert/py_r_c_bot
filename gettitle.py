import urllib.request
import html


def getPageTitle(url):
    try:
        site = urllib.request.urlopen(url)
        siteStr = site.read().decode('utf-8')

        usesTitleTag = True if siteStr.find('<title>') != -1 else False
        if usesTitleTag:
            title = siteStr.split('<title>')[1].split('</title>')[0]
            title = html.unescape(title)
            return title

        usesOpenGraph = True if siteStr.find('og:title') else False
        if usesOpenGraph:
            title = siteStr.split('og:title')[1].split(
                'content=')[1]
            splitChar = title[0]
            title = title.split(f"{splitChar}")[1]
            title = html.unescape(title)
            return title
    except:
        print(f'URL title lookup failed for {url}')
