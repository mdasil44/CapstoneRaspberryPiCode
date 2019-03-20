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

ALARM_LED = 24

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
wiringpi.pinMode(ALARM_LED,1)
wiringpi.pinMode(PIN_1,0)
wiringpi.digitalWrite(PIN_1,1)
wiringpi.pinMode(PIN_2,1)
wiringpi.pinMode(PIN_3,1)
wiringpi.pinMode(PIN_4,1)
wiringpi.pinMode(PIN_5,1)
wiringpi.pinMode(PIN_6,1)
wiringpi.pinMode(PIN_7,1)
wiringpi.pinMode(PIN_8,1)
wiringpi.pinMode(PIN_9,1)
wiringpi.pinMode(PIN_10,1)
wiringpi.pinMode(PIN_11,1)
wiringpi.pinMode(PIN_12,1)
wiringpi.pinMode(PIN_13,1)

print("Running")
count = 0;
try:
    while True:
        print(wiringpi.digitalRead(PIN_1))
except KeyboardInterrupt:
    
    pass