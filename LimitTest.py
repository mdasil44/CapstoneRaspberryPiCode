import wiringpi

PIN_1 = 29
PIN_2 = 28
PIN_3 = 27
PIN_4 = 25

wiringpi.wiringPiSetup()

wiringpi.pinMode(PIN_1,0) # X Limit
wiringpi.pinMode(PIN_2,0) # Y Limit
wiringpi.digitalWrite(PIN_2,0)
wiringpi.pinMode(PIN_3,0) # Alpha Limit
wiringpi.pinMode(PIN_4,0) # Theta Limit

while(True):
    hi = wiringpi.digitalRead(PIN_2)
    print(hi)
