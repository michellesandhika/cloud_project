from flask import Flask, render_template, request
import datetime
import mysql.connector
    
    
# modify the dmb connection credential here
def db_connection():
    mydb = mysql.connector.connect( 
        host = 'cloudcompproject.c5v4sxvaiqcz.us-east-1.rds.amazonaws.com',
        user = 'clouduser',
        port = '3306',
        database = '',
        password = 'cloudcomputing',
        autocommit = True
    )

    return mydb

mydb = db_connection()
cur = mydb.cursor()

# init flask app
application = Flask(__name__)

# routes
@application.route('/')
def index():
    drivers = ['likun1000003', 'haowei1000008', 'zouan1000007', 'zengpeng1000000', 'xiexiao1000001', 'shenxian1000004', 'panxian1000005', 'hanhui1000002', 'duxu1000009', 'xiezhi1000006']
    
    sql = "SELECT * FROM userTable.driverEvents";
    ret = cur.execute(sql)
    result = cur.fetchall()
    
    statistics = []
    summaryStatistics = [0,0,0,0,0,0,0,0]
    
    for driverNow in result:
        
        summaryStatistics[0] = summaryStatistics[0] + float(driverNow[6])
        summaryStatistics[1] = summaryStatistics[1] + float(driverNow[3])
        summaryStatistics[2] = summaryStatistics[2] + float(driverNow[7])
        summaryStatistics[3] = summaryStatistics[3] + float(driverNow[8])
        summaryStatistics[4] = summaryStatistics[4] + float(driverNow[9])
        summaryStatistics[5] = summaryStatistics[5] + float(driverNow[7])
        summaryStatistics[6] = summaryStatistics[6] + float(driverNow[2])
        summaryStatistics[7] = summaryStatistics[7] + float(driverNow[4])
        
        
        driverStatistics = {
                'id': driverNow[0],
                'plate': driverNow[1],
                'averageSpeed': driverNow[6],
                'countFatigueDriving': driverNow[3],
                'countHthrottleStop': driverNow[7],
                'countOilLeak': driverNow[8],
                'countNeutralSlide': driverNow[9],
                'totalNeutralSlide': driverNow[7],
                'countOverSpeed': driverNow[2],
                'totalOverSpeed': driverNow[4],
            },
        statistics.extend(driverStatistics)
        
    averageSpeed = summaryStatistics[0] / 10
    countFatigueDriving = summaryStatistics[1]  / 10
    countHthrottleStop = summaryStatistics[2] / 10
    countOilLeak = summaryStatistics[3] / 10
    countNeutralSlide = summaryStatistics[4] / 10
    totalNeutralSlide = summaryStatistics[5] / 10
    countOverSpeed = summaryStatistics[6] / 10
    totalOverSpeed = summaryStatistics[7] / 10
        
    data = {
        'id': '',
        'plate': '',
        'summary': {
            'averageSpeed': averageSpeed,
            'countFatigueDriving': countFatigueDriving,
            'countHthrottleStop': countHthrottleStop,
            'countOilLeak': countOilLeak,
            'countNeutralSlide': countNeutralSlide,
            'totalNeutralSlide': totalNeutralSlide,
            'countOverSpeed': countOverSpeed,
            'totalOverSpeed': totalOverSpeed,
        },
        'stats': statistics,
        'speed': [],
        'lastOverspeed': 0,
    }
    print(data)
    
    return render_template('index.html', drivers=drivers, data=data)


@application.route('/driver')
def driver():
    args = request.args.to_dict()
    driver = args['id']

    drivers = ['likun1000003', 'haowei1000008', 'zouan1000007', 'zengpeng1000000', 'xiexiao1000001', 'shenxian1000004', 'panxian1000005', 'hanhui1000002', 'duxu1000009', 'xiezhi1000006']
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
    
    args = request.args.to_dict()
    driver = args['id']
    
    speedArrayTotal = [['Date', 'Speed'], ["2017-1-1 08:00:00", 0]]
    data = {
        'id': driver,
        'plate': '华 AEB132',
        'summary': {},
        'stats': [],
        'speed': speedArrayTotal,
        'lastOverspeed': 0,
    }
    
    global date_and_time
    try:
        date_and_time
    except NameError:
        date_and_time = datetime.datetime(2017, 1, 1, 8, 0, 0)
        return data
    
    time_change = datetime.timedelta(seconds=30)
    new_time = date_and_time + time_change
    date_and_time = new_time
    
    sql = "SELECT * FROM userTable.partBTable WHERE driverID=\"{0}\" and time < \"{1}\";".format(driver,date_and_time)
    ret = cur.execute(sql)
    result = cur.fetchall()
    
    speedArrayTotal = []
    speedArrayTotal.append(['Date', 'Speed'])

    for i in range(0, len(result)):
        speedArray = []
        speedArray.append(result[i][2].strftime("%Y%m%d , %H:%M:%S"))
        speedArray.append(result[i][1])
        speedArrayTotal.append(speedArray)
        
    if (len(result) == 0):
        lastOverspeed = 0
    else:
        lastOverspeed = result[len(result)-1][3]
    
    data = {
        'speed': speedArrayTotal,
        'lastOverspeed': lastOverspeed,
    }

    return data


if __name__ == '__main__':
	application.run(port=5000, debug=True)