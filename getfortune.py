import random

# fortune list from: http://www.fortunecookiemessage.com/archive.php
fortunes = []

# load all the fortunes from the file fortunes.txt
def loadfortunes():
    my_file = open("fortunes.txt", "r")
    for line in my_file:
        fortunes.append(line.replace('\n', ''))

def printrandomfortune():
    random_index = random.randint(0, len(fortunes) - 1)
    return fortunes[random_index]

# test
# loadfortunes()
# printrandomfortune()