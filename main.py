# python irc bot
# based on a tutorial from: https://linuxacademy.com/blog/linux-academy/creating-an-irc-bot-with-python3/

import socket
import time
from datetime import datetime
# my files
import getweather
import getdate
import getfortune
import gettitle
import getskdtheme
import random
import time
import getmessages
import getartprompt
from getcovid import getCovidData
import getlols

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# create the chatbot
# chatbot = ChatBot('Nizz')
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net"
channel = "#bot-testing"
# channel = "#sketchdaily"
botnick = "nizztest"  # The bot's nickname
# My IRC nickname - change this to your username
adminname = ["teapup", "ThereIsNoJustice"]
exitcode = "bye " + botnick


def joinchannel(chan):
    ircsock.send(bytes("JOIN " + chan + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        if (ircmsg.strip() != ""):
            print(ircmsg)
    print(" > > > Channel successfully joined")


def ping():  # respond to server Pings
    ircsock.send(bytes("PONG :pingisn\n", "UTF-8"))


def sendmsg(msg, target=channel):  # sends messages to the target
    ircsock.send(bytes("PRIVMSG " + target + " :" + msg + "\n", "UTF-8"))


def main():
    random.seed()
    getfortune.loadfortunes()
    getlols.load()

    print(" > > > Beginning IRC bot")
    # connect to the server using the port 6667 (the standard IRC port)
    ircsock.connect((server, 6667))
    ircsock.send(
        bytes(
            "USER " + botnick + " " + botnick + " " + botnick + " " + botnick +
            "\n", "UTF-8"))
    # assign the nick to the bot
    ircsock.send(bytes("NICK " + botnick + "\n", "UTF-8"))
    print(" > > > Server joined")

    joinchannel(channel)
    while 1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        if (ircmsg.strip() != ""):
            print(ircmsg)

        messagerName = ircmsg.split('!', 1)[0][1:]

        if ircmsg.find("JOIN") != -1:
            # print(f'found join for username {name}')
            if getmessages.userHasMsg(messagerName):
                for messageNum in getmessages.msgDict[messagerName]:
                    message = getmessages.msgDict[messagerName][messageNum]
                    fromUser = message['from']
                    receivedMsg = message['msg']
                    sendmsg(f'{fromUser}: {receivedMsg}', messagerName)
                    time.sleep(5)
                del getmessages.msgDict[messagerName]
                time.sleep(5)
                sendmsg('these messages have self-destructed', messagerName)
                getmessages.saveMsgs()

        if ircmsg.find("PRIVMSG") != -1:
            message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
            if len(messagerName) < 17:

                # respond to 'hi <botname>'
                if message.find('hi ' + botnick) != -1 or message.find(
                        'hello ' +
                        botnick) != -1 or message.find('hey ' + botnick) != -1:
                    sendmsg("Hello " + messagerName + "!")
                elif messagerName in adminname and message.rstrip(
                ) == exitcode:  # quit with <exitcode>
                    sendmsg("oh...okay. :-/")
                    ircsock.send(bytes("QUIT\n", "UTF-8"))
                    return
                elif message.find(botnick) != -1 and random.randint(1, 5) == 1:
                    sendmsg("╚═།-◑-▃-◑-།═╝ beep boop")

                # respond to 'morning <botname>'
                if message.find('morning ' + botnick) != -1:
                    sendmsg("morning " + messagerName + "!")

                # use '..' to chat with the bot
                # if message.find('..') == 0:
                #     # get a response from chatbot
                #     msgNoPeriods = message.split('.')[2]
                #     response = chatbot.get_response(msgNoPeriods)
                #     response = str(response)
                #     print(response)
                #     sendmsg(response)

                if message.find('http') != -1:
                    splitMsg = message.split(' ')
                    for word in splitMsg:
                        if word.find('http') == 0:
                            foundTitle = gettitle.getPageTitle(word)
                            if foundTitle:
                                sendmsg(foundTitle)
                                time.sleep(1)

                # use '.tell' to send someone a message
                if message.find('.tell') == 0:
                    target = message.split(' ', 1)[1]
                    if target.find(' ') != -1:
                        message = target.split(' ', 1)[1]
                        target = target.split(' ')[0]
                    else:
                        target = messagerName
                        message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
                    sendmsg(message, target)

                if message.find('.msg') == 0:
                    try:
                        target = message.split(' ', 1)[1]
                        if target.find(' ') != -1:
                            message = target.split(' ', 1)[1]
                            target = target.split(' ')[0]
                            if (len(message) > 0):
                                getmessages.addMsg(
                                    target, messagerName, message)
                                sendmsg(
                                    f'your message has been stored until I see {target} join'
                                )
                            else:
                                sendmsg(
                                    "message should be sent in format: '.msg [target] [message]'"
                                )
                    except:
                        sendmsg(
                            "message should be sent in format: '.msg [target] [message]'"
                        )

                if message.find('.date') == 0:
                    # print("printing date")
                    sendmsg(getdate.printdaynumber())

                # SOMEDAY . . .
                # if message.find(".dodongo") == 0:
                #     sendmsg("!lol dodongo")

                if message.find(".ftoc") == 0:
                    try:
                        f = int(message.split(' ')[1])
                        c = (f - 32) / 1.8
                        c = format(c, ',.2f')
                        sendmsg(f"{f}f is {c}c")
                    except:
                        sendmsg("something went wrong")

                if message.find(".ctof") == 0:
                    try:
                        c = int(message.split(' ')[1])
                        f = (c * 1.8) + 32
                        f = format(f, ',.2f')
                        sendmsg(f"{c}c is {f}f")
                    except:
                        sendmsg("something went wrong")

                if message.find(".choose") == 0:
                    msgArrSplit = message.split(' ')
                    msgArrSplit.pop(0)
                    msgArrJoined = ' '.join(msgArrSplit)
                    msgArrCommaSplit = msgArrJoined.split(',')
                    # print(msgArrSplit)
                    if len(msgArrCommaSplit) == 1:
                        yesNos = [
                            "yeah do it", "do it right now", "definitely",
                            "absolutely",
                            "that's the best idea you've ever had",
                            "i order you to do it", "no i don't think so",
                            "terrible idea", "why even ask such a thing",
                            "eww no", "pft no",
                            "i order you to do something else"
                        ]
                        sendmsg(random.choice(yesNos))
                    elif len(msgArrCommaSplit) > 1:
                        # print(msgArrCommaSplit)
                        chosen = random.choice(msgArrCommaSplit)
                        preMsg = random.choice([
                            "i like this one", "sounds cool", "the best",
                            "be a good human",
                            "embrace obedience to your robot masters"
                        ])
                        messageToSend = f"{preMsg}: {chosen.strip()}"
                        # print(messageToSend)
                        sendmsg(messageToSend)
                    else:
                        sendmsg("you need to give me choices!!")

                if message.find('.artprompt') == 0:
                    splitMsg = message.split(' ')
                    if len(splitMsg) > 1:
                        promptType = splitMsg[1]
                        resLst = getartprompt.artPrompt(promptType)
                        if (len(resLst) > 1):
                            for msg in resLst:
                                sendmsg(msg, messagerName)
                                time.sleep(3)
                        else:
                            for msg in resLst:
                                sendmsg(msg)
                                time.sleep(3)
                    else:
                        sendmsg(
                            'One-line response: .artprompt <alignment/animegirl/creature/evilname/fantasyname/location/mecha/milunit/quickchar/title/tropescramble/vampirename>')
                        time.sleep(3)
                        sendmsg(
                            'Multi-line: .artprompt <catgirl/color/generalperson>')

                if message.find('.covid') == 0:
                    splitMsg = message.split(' ')
                    if len(splitMsg) > 1:
                        try:
                            zipcode = int(splitMsg[1])
                            reqDict = {"type": "zip", "code": zipcode}
                            sendmsg(getCovidData(reqDict))
                        except:
                            try:
                                countrycode = splitMsg[1].upper()
                                reqDict = {
                                    "type": "countrycode",
                                    "code": countrycode
                                }
                                sendmsg(getCovidData(reqDict))
                            except:
                                sendmsg('Something went wrong')
                    else:
                        sendmsg('.covid <zipcode/countrycode>')

                if message.find(".addloc") == 0:
                    splitmsg = message.lower().split(' ')
                    splitmsg.pop(0)
                    splitmsg = ' '.join(splitmsg).split(', ')
                    if len(splitmsg) == 3:
                        try:
                            city = splitmsg[0]
                            lat = float(splitmsg[1])
                            lon = float(splitmsg[2])
                            getweather.addLocation(city, lat, lon)
                            sendmsg('location added')
                        except:
                            sendmsg('Something went wrong')
                    else:
                        sendmsg('.addloc <location name>, <lat>, <lon>')

                if message.find(".weather") == 0:
                    # print("printing weather")
                    splitmsg = message.lower().split(' ')
                    splitmsg.pop(0)
                    splitmsg
                    cityName = ' '.join(splitmsg)
                    if len(splitmsg) >= 1:
                        sendmsg(getweather.printweather(cityName))
                    else:
                        sendmsg('.weather <location name>')

                if message.find(".fortune") == 0:
                    # print("printing fortune")
                    sendmsg(getfortune.printrandomfortune())

                if message.find('.getskdtheme') == 0:
                    # print('printing skd theme')
                    sendmsg(getskdtheme.printskdtheme())

                if message.find('.hotdog') == 0:
                    # print('printing a hotdog')
                    sendmsg('( ´∀｀)つ―⊂ZZZ⊃')

                if message.find('.addlol') == 0:
                    print('adding a lol')
                    splitmsg = message.split(' ', 1)
                    if len(splitmsg) <= 1:
                        sendmsg("which lol are you looking for?")
                    else:
                        lol = splitmsg[1].strip()
                        if lol != "":
                            sendmsg(
                                getlols.addlol(lol, messagerName,
                                               datetime.utcnow()))
                        else:
                            sendmsg("which lol are you looking for?")
                elif message.find('.searchlol') == 0:
                    print('searching for all lols matching a pattern')
                    splitmsg = message.split(' ', 1)
                    if len(splitmsg) > 1:
                        lol = splitmsg[1].strip()
                        if lol != "":
                            sendmsg(getlols.searchlol(splitmsg[1].strip()))
                        else:
                            sendmsg("which lol are you looking for?")
                    else:
                        sendmsg("which lol are you looking for?")
                elif message.find(".lolinfo") == 0:
                    print("searching for a lol")
                    splitmsg = message.split(' ', 1)
                    if len(splitmsg) > 1:
                        lol = splitmsg[1].strip()
                        if lol != "":
                            sendmsg(getlols.lolinfo(splitmsg[1].strip()))
                        else:
                            sendmsg("which lol are you looking for?")
                    else:
                        sendmsg("which lol are you looking for?")
                elif message.find('.lol') == 0:
                    print('looking up a lol')
                    splitmsg = message.split(' ', 1)
                    if len(splitmsg) > 1:
                        lol = splitmsg[1].strip()
                        if lol != "":
                            sendmsg(getlols.getlol(splitmsg[1].strip()))
                        else:
                            sendmsg("which lol are you looking for?")
                    else:
                        sendmsg("which lol are you looking for?")

                # if message.find(".weather") == 0: #old weather command
                #     print("printing weather")
                #     sendmsg(getweather.printweather(
                #         message[(len(".weather") + message.find(".weather")):]))

                # list of commands
                if message.find('.help') == 0:
                    sendmsg(
                        "COMMANDS: .addloc .addlol .lol .searchlol .covid .choose .ctof/.ftoc .date .fortune .hotdog .getskdtheme .weather"
                    )

        else:
            if ircmsg.find("PING :") != -1:
                ping()


while True:
    main()
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Waiting to attempt rejoin')
    time.sleep(120)
