# python irc bot
# based on a tutorial from: https://linuxacademy.com/blog/linux-academy/creating-an-irc-bot-with-python3/

import socket
import time
# my files
import getweather
import getdate
import getfortune
import getskdtheme
import random
import time
from getcovid import getCovidData


ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net"
channel = "#bot-testing"
# channel = "#sketchdaily"
botnick = "nizz"  # The bot's nickname
adminname = "teapup"  # My IRC nickname - change this to your username
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
    # getfortune.loadfortunes() #this is preventing the bot from running

    print(" > > > Beginning IRC bot")
    # connect to the server using the port 6667 (the standard IRC port)
    ircsock.connect((server, 6667))
    ircsock.send(bytes("USER " + botnick + " " + botnick +
                       " " + botnick + " " + botnick + "\n", "UTF-8"))
    # assign the nick to the bot
    ircsock.send(bytes("NICK " + botnick + "\n", "UTF-8"))
    print(" > > > Server joined")

    joinchannel(channel)
    while 1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        if (ircmsg.strip() != ""):
            print(ircmsg)

        # TODO: Use eval('text') to run code as a file that can be stopped without having to rejoin the IRC server

        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!', 1)[0][1:]
            message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1].lower()
            if len(name) < 17:

                # respond to 'hi <botname>'
                if message.find('hi ' + botnick.lower()) != -1 or message.find('hello ' + botnick.lower()) != -1 or message.find('hey ' + botnick.lower()) != -1:
                    sendmsg("Hello " + name + "!")
                elif name.lower() == adminname.lower() and message.rstrip() == exitcode:  # quit with <exitcode>
                    sendmsg("oh...okay. :-/")
                    ircsock.send(bytes("QUIT\n", "UTF-8"))
                    return
                elif message.find(botnick.lower()) != -1:
                    sendmsg("╚═།-◑-▃-◑-།═╝ beep boop")

                # use '.tell' to send someone a message
                if message.find('.tell') == 0:
                    target = message.split(' ', 1)[1]
                    if target.find(' ') != -1:
                        message = target.split(' ', 1)[1]
                        target = target.split(' ')[0]
                    else:
                        target = name
                        message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
                    sendmsg(message, target)

                # TODO: Make a table of 'name's (usernames) and additional corresponding info?

                if message.find('.date') == 0:
                    print("printing date")
                    sendmsg(getdate.printdaynumber())

                if message.find(".dodongo") == 0:
                    sendmsg("!lol dodongo")

                if message.find(".ftoc") == 0:
                    try:
                        f = int(message.split(' ')[1])
                        c = (f-32)/1.8
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
                    msgArrCommaSplit = msgArrJoined.split(', ')
                    print(msgArrSplit)
                    if len(msgArrCommaSplit) == 1:
                        yesNos = ["yeah do it", "well maybe",
                                  "no i don't think so", "it's probably fine"]
                        sendmsg(random.choice(yesNos))
                    elif len(msgArrCommaSplit) > 1:
                        print(msgArrCommaSplit)
                        chosen = random.choice(msgArrCommaSplit)
                        preMsg = random.choice(
                            ["i like this one", "sounds cool", "the best", "be a good human", "embrace obedience to your robot masters"])
                        messageToSend = f"{preMsg}: {chosen}"
                        print(messageToSend)
                        sendmsg(messageToSend)
                    else:
                        sendmsg("you need to give me choices!!")

                if message.find('.covid') != -1:
                    splitMsg = message.split(' ')
                    if len(splitMsg) > 1:
                        try:
                            zipcode = int(splitMsg[1])
                            reqDict = {"type": "zip", "code": zipcode}
                            sendmsg(getCovidData(reqDict))
                        except:
                            try:
                                countrycode = splitMsg[1].upper()
                                reqDict = {"type": "countrycode",
                                           "code": countrycode}
                                sendmsg(getCovidData(reqDict))
                            except:
                                sendmsg('Something went wrong')
                    else:
                        sendmsg('.covid <zipcode/countrycode>')

                if message.find(".addloc") == 0:
                    splitmsg = message.split(' ')
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
                    print("printing weather")
                    splitmsg = message.split(' ')
                    splitmsg.pop(0)
                    splitmsg = ' '.join(splitmsg).split(', ')
                    lat = 0
                    lon = 0
                    print(splitmsg)
                    if len(splitmsg) == 1:
                        loc = splitmsg[0]
                        sendmsg(getweather.printweather(loc, 0))
                    elif len(splitmsg) == 2:
                        try:
                            lat = int(splitmsg[0])
                            lon = int(splitmsg[1])
                            sendmsg(getweather.printweather(lat, lon))
                        except ValueError:
                            sendmsg("I couldn't do that!")
                    else:
                        sendmsg(
                            '.weather <location name> OR <latitude>, <longitude>')

                # if message.find(".fortune") == 0: #this prevents bot from running
                #     print("printing fortune")
                #     sendmsg(getfortune.printrandomfortune())

                if message.find('.getskdtheme') == 0:
                    print('printing skd theme')
                    sendmsg(getskdtheme.printskdtheme())

                if message.find('.hotdog') == 0:
                    print('printing a hotdog')
                    sendmsg('( ´∀｀)つ―⊂ZZZ⊃')

                # if message.find(".weather") == 0: #old weather command
                #     print("printing weather")
                #     sendmsg(getweather.printweather(
                #         message[(len(".weather") + message.find(".weather")):]))

                # list of commands
                if message.find('.help') == 0:
                    sendmsg(
                        "COMMANDS: .addloc .covid .choose .ctof/.ftoc .date .fortune .hotdog .getskdtheme .weather")

        else:
            if ircmsg.find("PING :") != -1:
                ping()


main()
