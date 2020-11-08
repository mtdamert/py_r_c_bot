import urllib.request
import random

# def convertInt(numStr):
#     numStr = numStr.split(',')
#     numStr = ''.join(numStr)
#     numStr = int(numStr)
#     return numStr


def shuffleList(lst):
    random.shuffle(lst)


def removeHtmlTags(tags, splitTag, html):
    tempString = html
    for tag in tags:
        tempString = ''.join(tempString.split(tag))
    retList = tempString.split(splitTag)
    last = retList.pop()
    return retList


def getColor():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=color")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        colors = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">'
        ], '</div>', siteHtml)
        shuffleList(colors)
        retLst = [colors[0], colors[1], colors[2]]
        return retLst
    except:
        return ["Error"]


def getMecha():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=mechamaker")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        mechas = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">'
        ], '</div>', siteHtml)
        shuffleList(mechas)
        retLst = [mechas[0], mechas[1], mechas[2]]
        return retLst
    except:
        return ["Error"]


def getRealAlignment():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=ralign")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('Alignments</div>')[1].split('<P>')[0].split(
            '<!--Title -->')[1]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        alignments = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)

        shuffleList(alignments)
        retLst = [alignments[0], alignments[1], alignments[2]]
        return retLst
    except:
        return ["Error"]


def artPrompt(promptType):
    try:
        retLst = []
        if promptType == "alignment":
            retLst = getRealAlignment()
        elif promptType == "mecha":
            retLst = getMecha()
        elif promptType == "color":
            retLst = getColor()
        else:
            retLst = ["Invalid prompt type!"]

        return retLst
    except:
        return ["Error"]
