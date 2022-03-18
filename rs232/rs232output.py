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
ser.isOpen()
# Reading the data from the serial port. This will be running in an infinite loop.

while True:
        # get keyboard input
        bytesToRead = ser.inWaiting()
        data = ser.read(bytesToRead)
        time.sleep(1)
        print(data)
        if len(list(bytes(data))) > 0 :
            all_data = data.decode(encoding="utf-8").split()
            print(all_data)
        # all_data[1]
        # print(array.array('B', [0xDE, 0xAD, 0xBE, 0xEF]))