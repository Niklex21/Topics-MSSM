from flask import Flask, render_template, request
import time
import serial
 
app = Flask(__name__)

serialCortex = serial.Serial(
	path = "/dev/ttyAMA0/",
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/left')
def left():
        serialCortex.write(bytes([4100]))
        return True

@app.route('/right')
def right():
        serialCortex.write(bytes([2100]))
        return True

@app.route('/fwd')
def fwd():
        serialCortex.write(bytes([1100]))
        return True

@app.route('/back')
def back():
        serialCortex.write(bytes([3100]))
        return True

@app.route('/stop')
def stop():
        serialCortex.write(bytes([100]))
        return True

if __name__ == "__main__":
	app.run(port = 80, host='0.0.0.0')
