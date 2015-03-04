import RPi.GPIO as GPIO
import time
import os
loop = 1
count = 10

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#while loop < 10:
#    input_state = GPIO.input(22)
#    if input_state == True:
#        print('Button Pressed')
#        #os.system('/airrif1_goodcut.wav &')
#        loop = loop + 1
#        time.sleep(3)
while True:
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    input_state = GPIO.input(22)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
