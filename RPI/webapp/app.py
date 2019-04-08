from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/left')
def left():
	return render_template('index.html', func_name = 'left')
	
@app.route('/right')
def right():
	return render_template('index.html', func_name = 'right')
	
@app.route('/back')
def back():
	return render_template('index.html', func_name = 'back')

@app.route('/fwd')
def fwd():
	return render_template('index.html', func_name = 'fwd')
	
@app.route('/stop')
def stop():
	return render_template('index.html', func_name = 'stop')


if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0', port = 8000)	
