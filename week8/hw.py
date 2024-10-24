import RPi.GPIO as GPIO
import threading
import serial
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24


bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)
gData = ""


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)


L_Motor = GPIO.PWM(PWMA, 500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB, 500)
R_Motor.start(0)


exit_event = threading.Event()


def serial_thread():
    global gData
    while not exit_event.is_set():
        try:
            data = bleSerial.readline()
            data = data.decode()
            gData = data
        except serial.SerialException as e:
            print(f"Serial read error: {e}")
            break


def main():
    global gData
    try:
        while True:
            if "go" in gData:
                gData = ""
                GPIO.output(AIN1, 0)
                GPIO.output(AIN2, 1)
                L_Motor.ChangeDutyCycle(50)
                GPIO.output(BIN1, 0)
                GPIO.output(BIN2, 1)
                R_Motor.ChangeDutyCycle(50)
                time.sleep(1.0)
            elif "right" in gData:
                gData = ""
                GPIO.output(AIN1, 0)
                GPIO.output(AIN2, 1)
                L_Motor.ChangeDutyCycle(50)
                GPIO.output(BIN1, 0)
                GPIO.output(BIN2, 1)
                R_Motor.ChangeDutyCycle(0)
                time.sleep(1.0)
            elif "left" in gData:
                gData = ""
                GPIO.output(AIN1, 0)
                GPIO.output(AIN2, 1)
                L_Motor.ChangeDutyCycle(0)
                GPIO.output(BIN1, 0)
                GPIO.output(BIN2, 1)
                R_Motor.ChangeDutyCycle(50)
                time.sleep(1.0)
            elif "back" in gData:
                gData = ""
                GPIO.output(AIN1, 1)
                GPIO.output(AIN2, 0)
                L_Motor.ChangeDutyCycle(50)
                GPIO.output(BIN1, 1)
                GPIO.output(BIN2, 0)
                R_Motor.ChangeDutyCycle(50)
                time.sleep(1.0)
            elif "stop" in gData:
                gData = ""
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)
                time.sleep(1.0)
            else:
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    try:
        task1 = threading.Thread(target=serial_thread)
        task1.start()
        main()
    finally:
        exit_event.set()  
        task1.join()  
        bleSerial.close()
        GPIO.cleanup()
        L_Motor.stop()
        R_Motor.stop()
