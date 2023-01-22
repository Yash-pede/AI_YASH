import serial

try:
    arduino = serial.Serial("COM3", 9600)
except:
    try:
        arduino = serial.Serial("COM4", 9600)
    except:
        pass

def arduniHI():
    arduino.write(b"H")


def arduinoLW():
    arduino.write(b"L")
