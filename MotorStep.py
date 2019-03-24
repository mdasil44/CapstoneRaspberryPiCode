def takeStep(motor, direction):
    STEP = 0
    DIR = 0
    
    switch(motor) {
        case 1: STEP = 22 # X Direction (Motor 1)
                DIR = 23
                break
        
        case 2: STEP = 14 # Y Direction (Motor 2)
                DIR = 13
                break
        
        case 3: STEP = 0 # Theta Rotation (Motor 3)
                DIR = 2
                break
        
        case 4: STEP = 12 # Alpha Rotation (Motor 4)
                DIR = 3
                break
    }
    
    wiringpi.digitalWrite(EN,0)
    
    wiringpi.digitalwrite(DIR,direction)
    
    wiringpi.digitalWrite(STEP,1)
    wiringpi.delayMicroseconds(400)
    wiringpi.digitalWrite(STEP,0)
    wiringpi.delayMicroseconds(400)
    
    wiringpi.digitalWrite(EN,0)