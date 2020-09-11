
# msgDict = {
#     "ThereIsNoJustice": {
#         0: {
#             "from": "tinj",
#             "msg": "hello testing hi",
#         },
#     },
# }

msgDict = {}


def loadMsgs():
    msg_file = open("msg.txt", "r")
    i = 0
    for line in msg_file:
        ln = line.strip('\n\r')
        print(ln)
        splitLine = ln.split(", ")
        receivingUser = splitLine[0]
        fromUser = splitLine[1]
        message = splitLine[2]
        msgDict[receivingUser] = {
            i: {
                "from": fromUser,
                "msg": message,
            }
        }
        i += 1
    print(msgDict)
    msg_file.close()


loadMsgs()


def saveMsgs():
    msg_file = open("msg.txt", "w+")
    msg_file.close()
    msg_file = open("msg.txt", "a+")
    for recUser in msgDict:
        for msgIdx in recUser:
            fromUser = msgDict[recUser][msgIdx]['from']
            message = msgDict[recUser][msgIdx]['msg']
            msg_file.write(f"{recUser}, {fromUser}, {message}\n")
    msg_file.close()


def addMsg(recUser, fromUser, msg):
    if recUser in msgDict:
        newMsgIdx = len(recUser.keys()) + 1
        msgDict[recUser][newMsgIdx] = {
            "from": fromUser,
            "msg": msg,
        }
    else:
      msgDict[recUser][0] = {
        "from": fromUser,
        "msg": msg,
      }
  saveMsgs()
