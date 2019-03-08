import serial 

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*

while True:
        serial_input = ser.readline()
        print(serial_input)
