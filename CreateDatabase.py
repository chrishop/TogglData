#CreateDatabase.py

import sqlite3
conn = sqlite3.connect("Toggl.db")
c=conn.cursor()

def CreateTable():
    c.execute("CREATE TABLE IF NOT EXISTS TogglTable("
              "Project TEXT,"
              "Description TEXT,"
              "StartDate TEXT,"
              "StartTime TEXT,"
              "EndDate TEXT,"
              "EndTime TEXT,"
              "Duration TEXT,"
              "Tags TEXT)")
    conn.commit()

CreateTable()