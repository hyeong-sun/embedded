import RPi.GPIO as GPIO
import time

SW1=5
SW2=6
SW3=13
SW4=19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True: 
        sw1Value=GPIO.input(SW1)
        sw2Value=GPIO.input(SW2)
        sw3Value=GPIO.input(SW3)
        sw4Value=GPIO.input(SW4)
        if(sw1Value==1):
            print("click 1")
            time.sleep(0.1)
        elif(sw2Value==1):
            print("click 2")  
            time.sleep(0.1)
        elif(sw3Value==1):
            print("click 3")  
            time.sleep(0.1)
        elif(sw4Value==1):
            print("click 4")  
            time.sleep(0.1)                       
        else :print(sw1Value) 
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
GPIO.cleanup()