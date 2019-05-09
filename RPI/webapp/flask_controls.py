from flask import Flask, render_template
from serial import Serial
 
app = Flask(__name__)

serialCortex = Serial(
	"/dev/serial0",
	baudrate = 9600,
	timeout = 1
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/left')
def left():
        serialCortex.write(bytes([4]))
        return render_template('index.html', func_name = 'left')

@app.route('/right')
def right():
        serialCortex.write(bytes([2]))
        return render_template('index.html', func_name = 'right')

@app.route('/fwd')
def fwd():
        serialCortex.write(bytes([1]))
        return render_template('index.html', func_name = 'fwd')

@app.route('/back')
def back():
        serialCortex.write(bytes([3]))
        return render_template('index.html', func_name = 'back')

@app.route('/stop')
def stop():
        serialCortex.write(bytes([0]))
        return render_template('index.html', func_name = 'stop')

if __name__ == "__main__":
        app.run(debug = True, host = '0.0.0.0', port = 8000)    
