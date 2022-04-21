import os
import sys 
import mysql.connector
from pyspark import SparkContext
import time
from datetime import datetime

starttime = datetime.now()
mydb = db_connection()
cur = mydb.cursor()

def db_connection():
	mydb = mysql.connector.connect(host = 'drivercloudproject.c5v4sxvaiqcz.us-east-1.rds.amazonaws.com',
		user='clouduser',
		port = '3306',
		passwd='driverdata',
		database='drivercloudproject',
		autocommit=True)

def senddata(data):
	# pad the data so its same size
	n = 19
	data += [''] * (n - len(data))

	sql = "insert into driverdata(driverID,carPlateNumber,Latitude,Longtitude,Speed,Direction,siteName,Time,isRapidlySpeedup,isRapidlySlowdown,isNeutralSlide,isNeutralSlideFinished,neutralSlideTime,isOverspeed,isOverspeedFinished,overspeedTime.isFatigueDriving,isHthrottleStop,isOilLeak) values ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18})".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18])
	ret = cur.execure(sql)



args = sys.argv
inp = args[1]
out = args[2]

# establish schema
#schema =["driverID","carPlateNumber","Latitude", "Longtitude","Speed","Direction","siteName","Time","isRapidlySpeedup","isRapidlySlowdown","isNeutralSlide","isNeutralSlideFinished","neutralSlideTime","isOverspeed","isOverspeedFinished","overspeedTime","isFatigueDriving","isHthrottleStop","isOilLeak"]

sc = SparkContext()
sqlContext = SQLContext(sc)


#reading the text file
text_file = sc.textFile(inp)
rdd = text_file.map(lambda line: line.split(","))

# insert raw data into sql
fulldata = rdd.map(lambda p:{"driverID":p[0],"carPlateNumber":p[1],"Latitude":p[2],"Longtitude":p[3],"Speed":p[4],"Direction":p[5],"siteName":p[6],"Time":p[7],"isRapidlySpeedup":p[8],"isRapidlySlowdown":p[9],"isNeutralSlide":p[10],"isNeutralSlideFinished":p[11],"neutralSlideTime":p[12],"isOverspeed":p[13],"isOverspeedFinished":p[14],"overspeedTime":p[15],"isFatigueDriving":p[16],"isHthrottleStop":p[17],"isOilLeak":p[18] })

while True:
	timedata = rdd.filter(lambda x: (starttime -timedelta(seconds =30)) < datetime.strptime(x[7],'%m-%d-%y %H:%M:%S') < starttime ).collect()
	starttime = starttime + timedelta(seconds = 30)
	for i in timedata:
		senddata(i)

rdd.saveAsTextFile(out)

sc.stop()