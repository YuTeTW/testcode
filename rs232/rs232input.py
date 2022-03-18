import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    timeout=1,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

while True:
        # get keyboard input
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        time.sleep(1)
        print(data)
        data2 = bytes([255, 250, 0, 1, 90, 90])
        print(ser.write(data2))
        print(data2)