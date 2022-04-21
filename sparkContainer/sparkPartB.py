import os
import sys 

from pyspark import SparkContext   
import mysql.connector

args = sys.argv
inp = args[1]

# establish schema
schema =["driverID","carPlateNumber","Latitude", "Longtitude","Speed","Direction","siteName","Time","isRapidlySpeedup","isRapidlySlowdown","isNeutralSlide","isNeutralSlideFinished","neutralSlideTime","isOverspeed","isOverspeedFinished","overspeedTime","isFatigueDriving","isHthrottleStop","isOilLeak"]

sc = SparkContext()

text_file = sc.textFile(inp)
rdd = text_file.map(lambda line: line.split(","))

rddFilterOverspeedTime = rdd.filter(lambda x: len(x) > 13)
rddFilterOverspeedTime = rddFilterOverspeedTime.map(lambda x: (x[0], x[3], x[7], 1) if (x[13] == "1") else ((x[0], x[3], x[7], -1) if (x[14] == "1") else (x[0], x[3], x[7], 0)))
resultSpeed = rddFilterOverspeedTime.collect()

rddFilterNoSpeed = rdd.filter(lambda x: len(x) < 9)
rddFilterNoSpeed = rddFilterNoSpeed.map(lambda x: (x[0], x[3], x[7], 0))
resultNoSpeed = rddFilterNoSpeed.collect()

sc.stop()

def db_connection():
    mydb = mysql.connector.connect( host = 'cloudcompproject.c5v4sxvaiqcz.us-east-1.rds.amazonaws.com',
    user = 'clouduser',
    port = '3306',
    database = '',
    passwd = 'cloudcomputing',
    autocommit = True)

    #print("successfully connect to the database")
    
    return mydb

mydb = db_connection()
cur = mydb.cursor()

for row in resultSpeed:
    sql = "insert into userTable.partBTable(driverID, speed, time, overspeed) values (\"{0}\", {1}, \"{2}\", {3});".format(row[0], row[1], row[2], row[3])
    ret = cur.execute(sql)
    
for row in resultNoSpeed:
    sql = "insert into userTable.partBTable(driverID, speed, time, overspeed) values (\"{0}\", {1}, \"{2}\", {3});".format(row[0], row[1], row[2], row[3])
    ret = cur.execute(sql)