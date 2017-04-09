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
    #print(first,last)

    #generate dates from first to last


    #fetches durations of dates
    sum_array = []
    for i in gen_dates():
        c.execute("SELECT Duration FROM TogglTable WHERE StartDate=?",(i,))
        data = c.fetchall()
        duration_summation = sum_duration(data)
        sum_array.append(duration_summation)
    return sum_array

def gen_dates():
    # select first  startdate and the laststart date
    c.execute("SELECT StartDate FROM TogglTable")
    data = c.fetchall()
    first = data[0][0]
    last = data[len(data) - 1][0]
    first_arr = [int(str(first[8:10])),int(str(first[5:7])),int(str(first[:4]))]
    last_arr = [int(str(last[8:10])), int(str(last[5:7])), int(str(last[:4]))]
    current = first_arr

    date_arr = [first]
    while current != last_arr:

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
            if current[1] is 2:
                # if its a leap year
                if int(current[2]) % 4 == 0 and (int(current[2]) % 100 == 0 or int(current[2]) % 400 == 0):
                    # its a leap year feb has 28 days
                    if current[0] <= 27:
                        current[0] += 1
                    else:
                        current[0] = 1
                        current[1] += 1

                else:
                    # feb has 29 days
                    if current[0] <= 28:
                        current[0] += 1
                    else:
                        current[0] = 1
                        current[1] += 1
            else:
                # normal 30 day month
                if current[0] <= 29:
                    current[0] += 1
                else:
                    current[0] = 1
                    current[1] += 1

        # format the date back into a string
        if len(str(current[0])) == 1:
            if len(str(current[1])) == 1:
                date = str(current[2]) + "-0" + str(current[1]) + "-0" + str(current[0])
            else:
                date = str(current[2]) + "-" + str(current[1]) + "-0" + str(current[0])
        else:
            if len(str(current[1])) == 1:
                date = str(current[2]) + "-0" + str(current[1]) + "-" + str(current[0])
            else:
                date = str(current[2]) + "-" + str(current[1]) + "-" + str(current[0])
        date_arr.append(date)
    return date_arr

def sum_duration(data):
    total_hours = 0
    total_mins = 0
    total_seconds = 0
    if data == []:
        return 0
    else:
        for i in data:
            hours = int(str(i[0])[:2])
            mins = int(str(i[0])[3:5])
            seconds = int(str(i[0])[6:8])

            total_hours += hours
            total_mins += mins
            total_seconds += seconds

        if total_seconds / 60 > 1:
            seconds = total_seconds % 60
            mins = total_mins + int(total_seconds / 60)
        if total_mins / 60 > 1:
            mins = total_mins % 60
            hours = total_hours + int(total_mins / 60)

    return hours*60 + mins



print(get_hours_day())


