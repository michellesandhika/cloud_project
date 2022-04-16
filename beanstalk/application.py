from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    # get query
    args = request.args.to_dict()
    driver = args['driver']

    # data format
    drivers = ['name01', 'name02', 'name03', 'name04', 'name05', 'name06', 'name07', 'name08', 'name09', 'name10']
    data = {
        'id': 'name02',
        'plate': '华 AEB132',
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
                'time': '2017-01-01 22:35:50',
                'latitude': '31.157939',
                'longtitude': '120.687431',
                'direction': '83',
                'siteName': 'n/a',
                'isRapidlySpeedup': '0',
                'isRapidlySlowDown': '1',
                'isNeutralSlide': '1',
                'isNeutralSlideFinished': '0',
                'neutralSlideTime': '10',
                'isOverSpeed': '0',
                'isOverSpeedFinished': '1',
                'overSpeedTime': '10',
                'isFatigueDriving': '1',
                'isHthrottleStop': '1',
                'isOilLeak': '1',
            },
            {
                'time': '2017-01-01 22:35:50',
                'latitude': '31.157939',
                'longtitude': '120.687431',
                'direction': '83',
                'siteName': 'n/a',
                'isRapidlySpeedup': '0',
                'isRapidlySlowDown': '1',
                'isNeutralSlide': '1',
                'isNeutralSlideFinished': '0',
                'neutralSlideTime': '10',
                'isOverSpeed': '0',
                'isOverSpeedFinished': '1',
                'overSpeedTime': '10',
                'isFatigueDriving': '1',
                'isHthrottleStop': '1',
                'isOilLeak': '1',
            }
        ],
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
	app.run(port=3000, debug=True)




