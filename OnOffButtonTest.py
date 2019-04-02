import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN_7 = 8 #PIN_7 = 10 for wiringpi, 8 for BCM
GPIO.setup(PIN_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

going = True;

def my_callback(channel):  
    global going
    print("Button Pressed")
    going = not going
    
GPIO.add_event_detect(PIN_7, GPIO.RISING, callback=my_callback, bouncetime=300)

while going:
    print("hi")