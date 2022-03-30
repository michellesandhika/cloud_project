from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    drivers = ['name01', 'name02', 'name03', 'name04', 'name05', 'name06', 'name07', 'name08', 'name09', 'name10']
    return render_template('index.html', title='Drivers', drivers=drivers)


if __name__ == '__main__':
	app.run(port=3000, debug=True)




