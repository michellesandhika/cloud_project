import os
import sys 

from pyspark import SparkContext

args = sys.argv
inp = args[1]
out = args[2]

# establish schema
schema =["driverID","carPlateNumber","Latitude", "Longtitude","Speed","Direction","siteName","Time","isRapidlySpeedup","isRapidlySlowdown","isNeutralSlide","isNeutralSlideFinished","neutralSlideTime","isOverspeed","isOverspeedFinished","overspeedTime","isFatigueDriving","isHthrottleStop","isOilLeak"]

sc = SparkContext()

text_file = sc.textFile(inp)
rdd = text_file.map(lambda line: line.split(","))
rdd.saveAsTextFile(out)

sc.stop()