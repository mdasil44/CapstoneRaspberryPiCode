import wiringpi

PIN_1 = 29
PIN_2 = 28
PIN_3 = 27
PIN_4 = 25

wiringpi.wiringPiSetup()

wiringpi.pinMode(PIN_1,0) # X Limit
wiringpi.pinMode(PIN_2,0) # Y Limit
wiringpi.pinMode(PIN_3,0) # Theta Limit
wiringpi.pinMode(PIN_4,0) # Alpha Limit

#this zeros the motors, pushing them to the limit switches and resetting the step count
#will then, after zeroing, return to the centre of the workspace
#initialize limit flags to LOW values
limitX = 0;
limitY = 0;
limitT = 0;
limitA = 0;
#make sure to get global values
global neutralX;
global neutralY;
global neutralTheta;
global neutralAlpha;
global midpointX;
global midpointY;
global xCounter;
global yCounter;
global thetaCount;
global alphaCount;
#loop while anything is not at the limit until everything is at limit switch
while (limitX == 0) or (limitY == 0) or (limitA == 0) or (limitT == 0):
    #read limit values
    limitX = wiringpi.digitalRead(PIN_1);
    limitY = wiringpi.digitalRead(PIN_2);
    limitA = wiringpi.digitalRead(PIN_3);
    limitT = wiringpi.digitalRead(PIN_4);
    #if values aren't HIGH, decrement step
    if (limitX != 1):
        takeStep(stepper.xTrans, dir.down);
    if (limitY != 1):
        takeStep(stepper.yTrans, dir.down);
    if (limitA != 1):
        takeStep(stepper.thetaRot, dir.down);
    if (limitT != 1):
        takeStep(stepper.alphaRot, dir.down);
#set counters to zero at this point
xCounter = 0;
yCounter = 0;
thetaCount = 0;
alphaCount = 0;
#loop until at mid point of everything
while (xCounter < midPointX) or (yCounter < midPointY) or (thetaCount < neutralTheta) or (alphaCount < neutralAlpha):
    if (xCounter < midPointX):
        takeStep(stepper.xTrans, dir.up);
        xCounter = xCounter + 1;
        neutralX = xCounter;
    if (yCounter < midPointY):
        takeStep(stepper.yTrans, dir.up);
        yCounter = yCounter + 1;
        neutralY = yCounter;
    if (thetaCount < neutralTheta):
        takeStep(stepper.thetaRot, dir.up);
        thetaCount = thetaCount + 1;
    if (alphaCount < neutralAlpha):
        takeStep(stepper.alphaRot, dir.up);
        alphaCount = alphaCount + 1;