import random
import os
from datetime import datetime

lols_file_loc = './data/lols.txt'
all_lols = {}

def load():
    # if the directory doesn't exist, create it
    if os.path.exists(lols_file_loc) is False:
        dir = os.path.dirname(lols_file_loc)
        if os.path.dirname(dir) is False:
            os.makedirs(dir)
    else:
        lols_file = open(lols_file_loc, "r", encoding="utf-8")
        new_lols = [line.rstrip().split(',', 1) for line in lols_file]
        lols_file.close()
        for line in new_lols:
            if len(line) > 1:
                # assume the line is in the format <key, value, author, date>
                text_parts = line[1].rsplit(',', 2)
                all_lols[line[0]] = {"value" : text_parts[0], "author" : text_parts[1], "time" : text_parts[2]}

def _addlol(key, value, author, time):
    key = key.strip()
    value = value.strip()
    # make sure this key isn't already used
    if key in all_lols:
        return "This LOL already exists!"

    time_str = time.strftime("%d/%m/%Y %H:%M:%S")
    lols_file = open(lols_file_loc, "a", encoding="utf-8")
    lols_file.write(key + "," + value + "," + author + "," + time_str + "\n")
    lols_file.close()
    all_lols[key] = {"value" : value, "author" : author, "time" : time_str}
    return "Yum yum, thanks!"

def addlol(line, author, time):
    # make sure that both a name and a value are provided
    if line.find(",") != -1:
        comma_pos = line.find(",")
        key = line[:comma_pos]
        value = line[(comma_pos + 1):]
        return _addlol(key, value, author, time)
    else:
        return "error, lol was not added. Example of how to add a lol: .addlol hotdog, ( ´∀｀)つ―⊂ZZZ⊃"

def getlol(lolname):
    if lolname in all_lols:
        return all_lols[lolname]["value"]
    else:
        return "nothing found"

def searchlol(lolname):
    lols_found = []
    for key,dictionary in all_lols.items():
        if lolname in key:
            lols_found.append(key)
    if len(lols_found) > 0:
        if len(lols_found) > 10:
            result = "first 10 possibilities: "
            for lol in lols_found:
                result += lol + ", "
            return result[:(len(result) - 2)]
        else:
            result = "possibilities: "
            for lol in lols_found:
                result += lol + ", "
            return result[:(len(result) - 2)]
    else:
        return "nothing found"

def lolinfo(lolname):
    if lolname in all_lols:
        return "author: " + all_lols[lolname]["author"] + ", added on: " + all_lols[lolname]["time"] + " UTC"
    else:
        return "LOL not found"
