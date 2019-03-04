from flask import Flask, render_template, request
import time
import serial
 
app = Flask(__name__)

leftMotor = 16 # motor output port number
rightMotor = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftMotor, GPIO.OUT)
GPIO.setup(rightMotor, GPIO.OUT)
GPIO.output(leftMotor , False)
GPIO.output(rightMotor, False)

port = "/dev/ttyACM0"
rate = 9600

arduino = serial.Serial(port, rate)
arduino.flushInput()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/left')
def left():
        GPIO.output(leftMotor, 0)
        GPIO.output(rightMotor, 1)
        return 'true'

@app.route('/right')
def right():
        GPIO.output(leftMotor, 1)
        GPIO.output(rightMotor, 0)

@app.route('/fwd')
def fwd():
        GPIO.output(leftMotor, 1)
        GPIO.output(rightMotor, 1)

@app.route('/back')
def back():
        GPIO.output(leftMotor, 0)
        GPIO.output(rightMotor, 0)

@app.route('/stop')
def stop():
        GPIO.output(leftMotor, 0)
        GPIO.output(rightMotor, 0)

if __name__ == "__main__":
	app.run(debug=True, port = 80, host='0.0.0.0')
