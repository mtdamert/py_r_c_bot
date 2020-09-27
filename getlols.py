import random
import os

lols_file_loc = '.\\data\\lols.txt'
all_lols = []

def load():
    # if the directory doesn't exist, create it
    if os.path.exists(lols_file_loc) is False:
        dir = os.path.dirname(lols_file_loc)
        if os.path.dirname(dir) is False:
            os.makedirs(dir)
    else:
        lols_file = open(lols_file_loc, "r")
        new_lols = [line.rstrip().split(',', 1) for line in lols_file]
        lols_file.close()
        for lol in new_lols:
            all_lols.append(lol)

def _addlol(key, value):
    key = key.strip()
    value = value.strip()
    # check that this exact lol doesn't already exist (remember that multiple lols can exist for the same key)
    for lol in all_lols:
        if lol[0] == key and lol[1] == value:
            return "This LOL already exists!"

    lols_file = open(lols_file_loc, "a")
    lols_file.write(key + "," + value + "\n")
    lols_file.close()
    all_lols.append([key, value])
    return "Yum yum, thanks!"

def addlol(line):
    # make sure that both a name and a value are provided
    if line.find(",") != -1:
        comma_pos = line.find(",")
        key = line[:comma_pos]
        value = line[(comma_pos + 1):]
        return _addlol(key, value)
    elif line.find(" ") != -1:
        space_pos = line.find(" ")
        key = line[:space_pos]
        value = line[(space_pos + 1):]
        return _addlol(key, value)
    else:
        return "error adding; example of hot to add a lol: .addlol hotdog, ( ´∀｀)つ―⊂ZZZ⊃"

def findlol(lolname):
    lols_found = []
    print("all lols:")
    print(all_lols)
    print("====")
    for lol in all_lols:
        print("checking against " + lol[0])
        if lol[0] == lolname:
            lols_found.append(lol)
    if len(lols_found) > 0:
        lol_num = random.randint(0, len(lols_found) - 1)
        return lols_found[lol_num][1]
    else:
        return "Nothing found"
