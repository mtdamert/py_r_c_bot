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


def getLocation():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=advname")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        location = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)
        shuffleList(location)
        retLst = [location[0]]
        return retLst
    except:
        return ["Error"]


def getAnimeGirl():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=afb")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        animeGirl = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)
        shuffleList(animeGirl)
        retLst = [animeGirl[0]]
        return retLst
    except:
        return ["Error"]


def getEvilName():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=evilnamer")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        evilName = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)
        shuffleList(evilName)
        retLst = [evilName[0]]
        return retLst
    except:
        return ["Error"]


def getTropeScramble():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=charscramble")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        tropeScramble = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">'
        ], '</div>', siteHtml)
        shuffleList(tropeScramble)
        retLst = [tropeScramble[0]]
        return retLst
    except:
        return ["Error"]


def getFantasyName():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=fantasynameex")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        fantasyName = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)
        shuffleList(fantasyName)
        retLst = [fantasyName[0]]
        return retLst
    except:
        return ["Error"]


def getMilUnit():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=fantasyunit")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        milUnit = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">'
        ], '</div>', siteHtml)
        shuffleList(milUnit)
        retLst = [milUnit[0]]
        return retLst
    except:
        return ["Error"]


def getCatGirl():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=catgirl")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        catGirl = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">',
            '"'
        ], '</div>', siteHtml)
        shuffleList(catGirl)
        catGirl[0] = catGirl[0].split('.')
        catGirl[0].pop()
        retLst = [*catGirl[0]]
        return retLst
    except:
        return ["Error"]


def getGeneralPerson():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=generalperson")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        generalPerson = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">'
        ], '</div>', siteHtml)
        shuffleList(generalPerson)
        generalPerson[0] = generalPerson[0].split('.')
        generalPerson[0].pop()
        retLst = [*generalPerson[0]]
        return retLst
    except:
        return ["Error"]


def getVampireName():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=vampnamer")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        creatures = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)
        shuffleList(creatures)
        retLst = [creatures[0]]
        return retLst
    except:
        return ["Error"]


def getCreature():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=legendcreature")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        creatures = removeHtmlTags([
            '<div class="GeneratorResultPrimeBGPara">',
            '<div class="GeneratorResultSecondaryBGPara">'
        ], '</div>', siteHtml)
        shuffleList(creatures)
        retLst = [creatures[0]]
        return retLst
    except:
        return ["Error"]


def getQuickChar():
    try:
        site = urllib.request.urlopen(
            "https://www.seventhsanctum.com/generate.php?Genname=quickchar")
        siteStr = site.read().decode('utf-8')

        siteHtml = siteStr.split('<!--Title -->')[2].split('<P>')[0]
        siteHtml = ''.join(siteHtml).strip('\n\r\t')
        quickChars = removeHtmlTags([
            '<div class="GeneratorResultPrimeBG">',
            '<div class="GeneratorResultSecondaryBG">'
        ], '</div>', siteHtml)
        shuffleList(quickChars)
        retLst = [quickChars[0]]
        return retLst
    except:
        return ["Error"]


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
        retLst = [mechas[0]]
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
        retLst = [alignments[0]]
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
        elif promptType == "generalperson":
            retLst = getGeneralPerson()
        elif promptType == "quickchar":
            retLst = getQuickChar()
        elif promptType == "creature":
            retLst = getCreature()
        elif promptType == "vampirename":
            retLst = getVampireName()
        elif promptType == "evilname":
            retLst = getEvilName()
        elif promptType == "tropescramble":
            retLst = getTropeScramble()
        elif promptType == "fantasyname":
            retLst = getFantasyName()
        elif promptType == "milunit":
            retLst = getMilUnit()
        elif promptType == "animegirl":
            retLst = getAnimeGirl()
        elif promptType == "catgirl":
            retLst = getCatGirl()
        elif promptType == "location":
            retLst = getLocation()
        else:
            retLst = ["Invalid prompt type!"]

        return retLst
    except:
        return ["Error"]
