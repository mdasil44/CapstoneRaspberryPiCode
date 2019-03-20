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