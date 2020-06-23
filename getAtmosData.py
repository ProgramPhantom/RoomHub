import serial

# COM3
try:
    serialPort = serial.Serial(port="COM3", baudrate=9600,
                               bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except serial.serialutil.SerialException:
    raise Exception("Arduino not plugged in noob.")

temp = "0"
humid = "0"

dic = {"humidity": "0", "temperature": "0"}


def getTemps():
    global dic
    if serialPort.in_waiting > 0:
        data = serialPort.readline().decode("Ascii").strip()
        print(data)
        dic = eval(data)
        print("New data in!", dic)
        return dic

    else:
        print("Missed data")
        return dic
