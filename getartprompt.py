import urllib.request

# def convertInt(numStr):
#     numStr = numStr.split(',')
#     numStr = ''.join(numStr)
#     numStr = int(numStr)
#     return numStr

def removeHtmlTags(tags, splitTag, html):
  tempString = html
  for tag in tags:
    tempString = ''.join(tempString.split(tag))
  retList = tempString.split(splitTag)
  return retList

def getRealAlignment():
  try:
      site = urllib.request.urlopen("https://www.seventhsanctum.com/generate.php?Genname=ralign")
      siteStr = site.read().decode('utf-8')

      siteHtml = siteStr.split('Alignments</div>')[1].split('<P>')[0].split('<!--Title -->')[1]
      siteHtml = ''.join(siteHtml).strip('\n\r\t')
      retStr = removeHtmlTags(
        ['<div class="GeneratorResultPrimeBG">',
         '<div class="GeneratorResultSecondaryBG">'],
         '</div>',
         siteHtml)

      return retStr
  except:
    return "Error"


def artPrompt(promptType):
    try:
        retStr = getRealAlignment() if promptType == "alignment" else getMecha() if promptType == "mecha" else "Invalid prompt type!"

        return retStr
    except:
        return "Error"


print(artPrompt("alignment"))
# print(artPrompt("sdfsfd"))
