import RPi.GPIO as GPIO
import time

SW1 = 5  
SW2 = 6  
SW3 = 13 
SW4 = 19 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

click_count = {SW1: 0, SW2: 0, SW3: 0, SW4: 0}

try: 
    while True: 
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)

        if sw1Value == 1: 
            click_count[SW1] += 1
            print(f"('SW1 click', {click_count[SW1]})")
            time.sleep(0.1)  

        elif sw2Value == 1: 
            click_count[SW2] += 1
            print(f"('SW2 click', {click_count[SW2]})")
            time.sleep(0.1)  

        elif sw3Value == 1: 
            click_count[SW3] += 1
            print(f"('SW3 click', {click_count[SW3]})")
            time.sleep(0.1) 

        elif sw4Value == 1:  
            click_count[SW4] += 1
            print(f"('SW4 click', {click_count[SW4]})")
            time.sleep(0.1)  

        time.sleep(0.1) 

except KeyboardInterrupt:
    pass
    GPIO.cleanup()  
