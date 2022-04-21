from flask import Flask, render_template, request
import datetime
from turtle import speed
import mysql.connector
import json
from time import time, sleep
from http import cookies
    
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

# init flask app
application = Flask(__name__)

# routes
@application.route('/')
def index():
    drivers = ['name01', 'name02', 'name03', 'name04', 'name05', 'name06', 'name07', 'name08', 'name09', 'name10']
    data = {
        'id': '',
        'plate': '',
        'summary': {
            'averageSpeed': '1',
            'countFatigueDriving': '2',
            'countHthrottleStop': '3',
            'countOilLeak': '4',
            'countNeutralSlide': '5',
            'totalNeutralSlide': '6',
            'countOverSpeed': '7',
            'totalOverSpeed': '8',
        },
        'stats': [
            {
                'id': 'name01',
                'plate': '华 AEB132',
                'averageSpeed': '1',
                'countFatigueDriving': '2',
                'countHthrottleStop': '3',
                'countOilLeak': '4',
                'countNeutralSlide': '5',
                'totalNeutralSlide': '6',
                'countOverSpeed': '7',
                'totalOverSpeed': '8',
            },
            {
                'id': 'name02',
                'plate': '华 AEB132',
                'averageSpeed': '1',
                'countFatigueDriving': '2',
                'countHthrottleStop': '3',
                'countOilLeak': '4',
                'countNeutralSlide': '5',
                'totalNeutralSlide': '6',
                'countOverSpeed': '7',
                'totalOverSpeed': '8',
            }
        ],
        'speed': []
    }
    
    return render_template('index.html', drivers=drivers, data=data)

@application.route('/driver')
def driver():
    # get query
    args = request.args.to_dict()
    driver = args['id']

    # data format
    drivers = ['name01', 'name02', 'name03', 'name04', 'name05', 'name06', 'name07', 'name08', 'name09', 'name10']
    
    # data format
    # drivers = ['likun1000003', 'haowei1000008', 'zouan1000007', 'zengpeng1000000', 'xiexiao1000001', 'shenxian1000004', 'panxian1000005', 'hanhui1000002', 'duxu1000009', 'xiezhi1000006']
    
    speedArrayTotal = [['Date', 'Speed'], ["2017-1-1 08:00:00", 0]]
    
    data = {
        'id': driver,
        'plate': '华 AEB132',
        'summary': {},
        'stats': [],
        'speed': speedArrayTotal,
        'lastOverspeed': 0,
    }
    
    return render_template('index.html', drivers=drivers, data=data)
    
@application.route('/data')
def getData():
    global date_and_time
    try:
        date_and_time
    except NameError:
        date_and_time = datetime.datetime(2017, 1, 1, 8, 0, 0)
    lastTime = datetime.datetime(2017, 1, 1, 23, 59, 59) 
    
    time_change = datetime.timedelta(seconds=30)
    new_time = date_and_time + time_change
    date_and_time = new_time
    print(date_and_time)
    
    sql = "SELECT * FROM userTable.partBTable WHERE driverID=\"{0}\" and time < \"{1}\";".format("likun1000003",date_and_time)
    ret = cur.execute(sql)
    result = cur.fetchall()
    print(result)
    
    speedArrayTotal = []
    speedArrayTotal.append(['Date', 'Speed'])

    for i in range(0, len(result)):
        speedArray = []
        speedArray.append(result[i][2].strftime("%Y%m%d , %H:%M:%S"))
        speedArray.append(result[i][1])
        speedArrayTotal.append(speedArray)
        
    if len(result) == 0:
        lastOverspeed = 0
    else:
        lastOverspeed = result[len(result)-1][3]
    print(speedArrayTotal)
    
    data = {
        'speed': speedArrayTotal,
        'lastOverspeed': lastOverspeed,
    }

    return data


if __name__ == '__main__':
	application.run(port=5000, debug=True)
