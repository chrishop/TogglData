#csvhandler.py

import sqlite3
conn = sqlite3.connect("Toggl.db")
c = conn.cursor()

def csv_To_Array(filename):
    array = []
    f = open(filename,"r")
    lineout = "has to be filled"
    while lineout != "":
        lineout = f.readline()
        array.append(lineout.split(","))
    return array

def enter_toggl_table(project,timeestimate,task,subtask,startdate,starttime,enddate,endtime,duration,tags):
    c.execute("INSERT INTO TogglTable("
              "Project,TimeEstimate,SubTask,Task,StartDate,StartTime,EndDate,EndTime,Duration,Tags) "
              "VALUES(?,?,?,?,?,?,?,?,?,?)",(project,
                                             timeestimate,
                                             task,subtask,
                                             startdate,
                                             starttime,
                                             enddate,
                                             endtime,
                                             duration,
                                             tags))
    conn.commit()

def csv_to_database(cvs_filename):
    array = csv_To_Array(cvs_filename)
    for i in range(1,len(array)-1):
        print(i)
        enter_toggl_table(array[i][3],str(array[i][5])[1:],array[i][6],str(array[i][7])[:len(array[i][7])-1],array[i][9],array[i][10],array[i][11],array[i][12],array[i][13],array[i][14])

print(csv_To_Array("TogglRaw.csv"))
csv_to_database("TogglRaw.csv")