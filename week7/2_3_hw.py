import RPi.GPIO as GPIO
import time

BUZZER=12
SW1=5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER,GPIO.OUT)

p=GPIO.PWM(BUZZER,261)
p.start(50)

try:
    while True:
        sw1Value=GPIO.input(SW1)
        if sw1Value==1:
            p.start(50)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(261)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(261)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.ChangeFrequency(261)
            time.sleep(0.5)

            p.stop()
            time.sleep(1.0)
        else : p.stop(0.1)
        
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()