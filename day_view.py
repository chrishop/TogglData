import matplotlib.pyplot as plt
import numpy as np
import sqlite3

conn = sqlite3.connect("Toggl.db")
c = conn.cursor()

def get_hours_day():
    #select first  startdate and the laststart date
    c.execute("SELECT StartDate FROM TogglTable")
    data = c.fetchall()
    first = data[0][0]
    last = data[len(data)-1][0]
    print(first,last)

    #generate dates from first to last


    #fetches durations of dates
    for i in dates:
        c.execute("SELECT Duration FROM TogglTable WHERE StartDate=?",(i[0],))
        data = c.fetchall()
        print(data)

def gen_dates():
    # select first  startdate and the laststart date
    c.execute("SELECT StartDate FROM TogglTable")
    data = c.fetchall()
    first = data[0][0]
    last = data[len(data) - 1][0]
    first = [int(str(first[8:10])),int(str(first[5:7])),int(str(first[:4]))]
    last = [int(str(last[8:10])), int(str(last[5:7])), int(str(last[:4]))]
    current = first
    print(current,last)

    date_arr = ["null"]
    while date_arr[len(date_arr)-1] != last:

        # if its a month with 31 days
        if current[1] is 1 or current[1] is 3 or current[1] is 5 or current[1] is 7 or current[1] is 8 or current[1] is 10 or current[1] is 12:
            # its a month with 31 days
            if current[0] <= 30:
                current[0] += 1
            else:
                # if last month of year

                if current[1] == 12:
                    current = [1, 1, current[2] + 1]
                else:
                    current[0] = 1
                    current[1] += 1


        else:
            # if its a month with 30 days
            # if its feb
            print("30 days")
            if current[1] is 2:
                #if its a leap year
                if int(current[2]) % 4 == 0:
                    if int(current[2]) % 100 == 0 or int(current[2]) % 400 == 0:
                        # its a leap year feb has 28 days
                        if current[0] <= 28:
                            print("eeek")
                            current[0] += 1
                        else:
                            current[0] = 1
                            current[1] += 1

                    else:
                        # feb has 29 days
                        if current[0] <= 29:
                            current[0] += 1
                        else:
                            current[0] = 1
                            current[1] += 1
            else:
                #normal 30 day month
                if current <= 30:
                    current[0] += 1
                else:
                    current[0] = 1
                    current[1] += 1
        print(current)
        date_arr.append(current)




gen_dates()
