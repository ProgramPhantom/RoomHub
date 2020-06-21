import serial

# COM3
serialPort = serial.Serial(port="/dev/ttyS3", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


def getTemps():
    if serialPort.in_waiting > 0:
        temp = serialPort.readline()
        return temp.decode("Ascii")
