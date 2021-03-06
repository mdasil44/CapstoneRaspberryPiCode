import wiringpi

EN = 21
DIR_1 = 23
STEP_1 = 22
DIR_2 = 13
STEP_2 = 14
DIR_3 = 2
STEP_3 = 0
DIR_4 = 3
STEP_4 = 12

#ALARM_LED = 24

# 16-pin connector to GPIO w/ 1 being the pin closest to the red led
PIN_1 = 29
PIN_2 = 28
PIN_3 = 27
PIN_4 = 25
PIN_5 = 26
PIN_6 = 11
PIN_7 = 10
PIN_8 = 6
PIN_9 = 5
PIN_10 = 4
PIN_11 = 1
PIN_12 = 16
PIN_13 = 15
# Pins 14-16 were not connected in the 16 pin connector
# In current implementation, 3.3V will be directly wired to the 16th pin and GND to the 15th pin

wiringpi.wiringPiSetup()

wiringpi.pinMode(EN,1)
wiringpi.pinMode(STEP_1,1)
wiringpi.pinMode(DIR_1,1)
wiringpi.digitalWrite(DIR_1,1)
wiringpi.pinMode(STEP_2,1)
wiringpi.pinMode(DIR_2,1)
wiringpi.digitalWrite(DIR_2,1)
wiringpi.pinMode(STEP_3,1)
wiringpi.pinMode(DIR_3,1)
wiringpi.digitalWrite(DIR_3,1)
wiringpi.pinMode(STEP_4,1)
wiringpi.pinMode(DIR_4,1)
wiringpi.digitalWrite(DIR_4,1)
#wiringpi.pinMode(ALARM_LED,1)
#wiringpi.pinMode(PIN_1,0)
#wiringpi.pinMode(PIN_2,0)
wiringpi.pinMode(PIN_5,1)
wiringpi.pinMode(PIN_6,1)
wiringpi.pinMode(PIN_3,1)
wiringpi.pinMode(PIN_4,1)
wiringpi.digitalWrite(PIN_3,0) # Alpha Limit
wiringpi.digitalWrite(PIN_4,0) # Theta Limit
wiringpi.digitalWrite(PIN_5,0) # X Limit
wiringpi.digitalWrite(PIN_6,0) # Y Limit
#wiringpi.pinMode(PIN_7,1)
#wiringpi.pinMode(PIN_8,1)
#wiringpi.pinMode(PIN_9,1)
#wiringpi.pinMode(PIN_10,1)
#wiringpi.pinMode(PIN_11,1)
#wiringpi.pinMode(PIN_12,1)
#wiringpi.pinMode(PIN_13,1)

print("Running")
count = 0;
try:
    while True:
        x = wiringpi.digitalRead(PIN_5)
        y = wiringpi.digitalRead(PIN_6)
        alpha = wiringpi.digitalRead(PIN_3)
        theta = wiringpi.digitalRead(PIN_4)
        
        if x == 1:
            print("x")
        if y == 1:
            print("y")
        if alpha == 1:
            print("alpha")
        if theta == 1:
            print("theta")
        wiringpi.digitalWrite(EN,0)
        temp = input("X: Press 'q' to step positive, press 'w' to step negative\nY: Press 'a' to step positive, press 's' to step negative\nAlpha (upper swing): Press 'e' to rotate positive, press 'r' to rotate negative\nTheta (lower swing): Press 'd' to rotate positive, press 'f' to rotate negative\n")
        if (temp == "q" or temp == "w"): # and x == 0:
#            wiringpi.digitalWrite(EN,0)
            if temp == "q":
                wiringpi.digitalWrite(DIR_1,0)
            else:
                wiringpi.digitalWrite(DIR_1,1)
            for x in range(20):
                for y in range(10):
                    wiringpi.digitalWrite(STEP_1,1)
                    wiringpi.delayMicroseconds(400)
                    wiringpi.digitalWrite(STEP_1,0)
                    wiringpi.delayMicroseconds(400)
#            wiringpi.digitalWrite(EN,1)
        elif (temp == "a" or temp == "s"): # and y == 0:
#            wiringpi.digitalWrite(EN,0)
            if temp == "a":
                wiringpi.digitalWrite(DIR_2,0)
            else:
                wiringpi.digitalWrite(DIR_2,1)
            for x in range(20):
                for y in range(10):
                    wiringpi.digitalWrite(STEP_2,1)
                    wiringpi.delayMicroseconds(400)
                    wiringpi.digitalWrite(STEP_2,0)
                    wiringpi.delayMicroseconds(400)
#            wiringpi.digitalWrite(EN,1)
        elif (temp == "e" or temp == "r"): # and alpha == 0:
#            wiringpi.digitalWrite(EN,0)
            if temp == "e":
                wiringpi.digitalWrite(DIR_3,0)
            else:
                wiringpi.digitalWrite(DIR_3,1)
            for x in range(5):
                wiringpi.digitalWrite(STEP_3,1)
                wiringpi.delayMicroseconds(500)
                wiringpi.digitalWrite(STEP_3,0)
                wiringpi.delayMicroseconds(500)
#            wiringpi.digitalWrite(EN,1)
        elif (temp == "d" or temp == "f"): #and theta == 0:
#            wiringpi.digitalWrite(EN,0)
            if temp == "d":
                wiringpi.digitalWrite(DIR_4,0)
            else:
                wiringpi.digitalWrite(DIR_4,1)
            for x in range(5):
                wiringpi.digitalWrite(STEP_4,1)
                wiringpi.delayMicroseconds(400)
                wiringpi.digitalWrite(STEP_4,0)
                wiringpi.delayMicroseconds(400)
#            wiringpi.digitalWrite(EN,1)
except KeyboardInterrupt:
    wiringpi.digitalWrite(STEP_1,0)
    wiringpi.digitalWrite(STEP_2,0)
    wiringpi.digitalWrite(STEP_3,0)
    wiringpi.digitalWrite(STEP_4,0)
    wiringpi.digitalWrite(EN,1)
    pass