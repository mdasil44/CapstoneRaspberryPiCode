import wiringpi

PIN_5 = 26
PIN_6 = 11
PIN_3 = 27
PIN_4 = 25
PIN_7 = 10

wiringpi.wiringPiSetup()

wiringpi.pinMode(PIN_5,0) # X Limit
wiringpi.pinMode(PIN_6,1) # Y Limit
wiringpi.digitalWrite(PIN_6,0)
#wiringpi.pinMode(PIN_6,0)
wiringpi.pinMode(PIN_3,0) # Alpha Limit
wiringpi.pinMode(PIN_4,0) # Theta Limit
wiringpi.pinMode(PIN_7,1) # Y Limit
wiringpi.digitalWrite(PIN_7,0)

while(True):
    hi = wiringpi.digitalRead(PIN_7)
#    hi2 = wiringpi.digitalRead(PIN_6)
    print(hi)
