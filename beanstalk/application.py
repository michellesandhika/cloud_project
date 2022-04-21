from flask import Flask, render_template, request

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
    data = {
        'id': 'name01',
        'plate': '华 AEB132',
        'summary': {},
        'stats': [],
        'speed': [
            ['Date', 'Speed'],
            ['2017-01-01 22:35:50', 66],
            ['2017-01-01 22:35:50', 68],
            ['2017-01-01 22:35:50', 68],
            ['2017-01-01 22:35:50', 68],
            ['2017-01-01 22:35:50', 68],
        ],
    }

    return render_template('index.html', drivers=drivers, data=data)


if __name__ == '__main__':
	application.run(port=5000, debug=True)




