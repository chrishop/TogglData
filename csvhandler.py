#csvhandler.py

def CvsToArray(filename):
    array = []
    f = open(filename,"r")
    lineout = "has to be filled"
    while lineout != "":
        lineout = f.readline()
        array.append(lineout.split(","))
    return array







print(CvsToArray("TogglRaw.csv"))