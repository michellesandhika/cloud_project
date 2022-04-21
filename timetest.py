import datetime
from turtle import speed
import mysql.connector
import json
from time import time, sleep

def db_connection():
   mydb = mysql.connector.connect( host = 'cloudcompproject.c5v4sxvaiqcz.us-east-1.rds.amazonaws.com',
   user = 'clouduser',
   port = '3306',
   database = '',
   passwd = 'cloudcomputing',
   autocommit = True)
   
   return mydb

mydb = db_connection()
cur = mydb.cursor()

date_and_time = datetime.datetime(2017, 1, 1, 8, 0, 0)
global new_time
lastTime = datetime.datetime(2017, 1, 1, 23, 59, 59)

time_change = datetime.timedelta(minutes=5)
new_time = date_and_time + time_change
date_and_time = new_time
   
sql = "SELECT * FROM userTable.partBTable WHERE driverID=\"likun1000003\" and time < \"{0}\";".format(date_and_time)
ret = cur.execute(sql)
result = cur.fetchall()
print(result)


# while date_and_time < lastTime:
#    sleep(30 - time() % 30)
#    time_change = datetime.timedelta(seconds=30)
#    new_time = date_and_time + time_change
#    date_and_time = new_time
   
#    sql = "SELECT * FROM userTable.partBTable WHERE driverID=\"likun1000003\" and time < \"{0}\";".format(date_and_time)
#    ret = cur.execute(sql)
#    result = cur.fetchall()
   
#    speedArrayTotal = []
#    speedArrayTotal.append(['Date', 'Speed'])

#    for i in range(0, len(result)):
#       speedArray = []
#       speedArray.append(result[i][1])
#       speedArray.append(result[i][2].strftime("%Y%m%d , %H:%M:%S"))
#       speedArrayTotal.append(speedArray)
      
#    lastOverspeed = result[len(result)-1][3]

#    data = {
#          'lastOverspped': lastOverspeed,
#          'speed': speedArrayTotal,
#       }
   
   
   
