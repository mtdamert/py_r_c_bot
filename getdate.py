from datetime import datetime

def getmonthstr(monthnum):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(monthnum, "Invalid month")

def getordinalnumberstr(num):
  if num % 10 == 1 and num != 11:
    return str(num) + "st"
  elif num % 10 == 2 and num != 12:
    return str(num) + "nd"
  elif num % 10 == 3 and num != 13:
    return str(num) + "rd"
  else:
    return str(num) + "th"

def getneattodaydate(now):
    return getmonthstr(now.month) + " " + getordinalnumberstr(now.day)

def printdaynumber():
  now = datetime.now()

  return ("It's " + getneattodaydate(now) +  ", the " + getordinalnumberstr(now.timetuple().tm_yday) + " day of the year")
  