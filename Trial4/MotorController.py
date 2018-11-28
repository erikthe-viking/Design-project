import ASUS.GPIO as GPIO
import time
import threading

class MotorController:

    def __init__(self):
#define shuffler pin constants
        self.ShufflerPWMPin = 33
        self.ShufflerIn1Pin = 3
        self.ShufflerIn2Pin = 5

#define base motor pin constants
        self.BaseMS1Pin    = 7
        self.BaseMS2Pin    = 8
        self.BaseDirPin    = 10
        self.BaseStepPin   = 11
        self.BaseEnablePin = 12

#define flipper motor pin constants
        self.CardWheelStepPins = [13, 15, 16, 18]
        self.TrackStepPins     = [19, 21, 22, 23]

#define stepper motor sequence
        self.StepSequence = [[1,0,0,1],
                             [1,0,0,0],
                             [1,1,0,0],
                             [0,1,0,0],
                             [0,1,1,0],
                             [0,0,1,0],
                             [0,0,1,1],
                             [0,0,0,1]]
#MS1 MS2
#L   L  =full step (2 phase)
#H   L  =half step 
#L   H  =quarter step 
#H   H  =eigth step 

#setup control pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.ShufflerPWMPin, GPIO.OUT)
        GPIO.setup(self.ShufflerIn1Pin, GPIO.OUT)
        GPIO.setup(self.ShufflerIn2Pin, GPIO.OUT)
        GPIO.setup(self.BaseMS1Pin, GPIO.OUT)
        GPIO.setup(self.BaseMS2Pin, GPIO.OUT)
        GPIO.setup(self.BaseDirPin, GPIO.OUT)
        GPIO.setup(self.BaseStepPin, GPIO.OUT)
        GPIO.setup(self.BaseEnablePin, GPIO.OUT)

        for pin in self.CardWheelStepPins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        for pin in self.TrackStepPins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

#init base motor pins 
        self.ResetBaseMotorPins()

#set up PWM speed control (50hz for now, may change)
        self.ShufflerSpeedControl = GPIO.PWM(self.ShufflerPWMPin, 50)
        
#run the shuffler instantaneously (use a sleep statement or call in loop)
    def RunShuffler(self, dutyCycle):
        self.ShufflerSpeedControl.ChangeDutyCycle(dutyCycle)
        GPIO.output(self.ShufflerIn1Pin, True)
        GPIO.output(self.ShufflerIn2Pin, False)

    def StopShuffler(self):
        GPIO.output(self.ShufflerIn1Pin, False)
        GPIO.output(self.ShufflerIn2Pin, False)
        
    def ResetBaseMotorPins(self):
        GPIO.output(self.BaseStepPin, False)
        GPIO.output(self.BaseDirPin, False)
        GPIO.output(self.BaseMS1Pin, False)
        GPIO.output(self.BaseMS2Pin, False)
        GPIO.output(self.BaseEnablePin, True)

    def RotateBase(self, numDegrees, direction):
        numSteps = int(round(numDegrees / 1.8))
        GPIO.output(self.BaseEnablePin, False)
        if direction == "clockwise":
            GPIO.output(self.BaseDirPin, False)
        else:
            GPIO.output(self.BaseDirPin, True)

        for i in range (0, numSteps):
            GPIO.output(self.BaseStepPin, True)
            time.sleep(0.005)
            GPIO.output(self.BaseStepPin, False)

    def RotateStepper(self, motorName, numDegrees, direction, stepDelay):
        print("running", motorName, direction, "by", numDegrees, stepDelay)
        if motorName == "card wheel":
            stepperPinList = self.CardWheelStepPins
        elif motorName == "track":
            stepperPinList = self.TrackStepPins

        numSteps = int(round(numDegrees / 5.625 * 8))
        for i in range (numSteps):
            if direction == "clockwise":
                for j in range(8):
                    self.SetStepperMotorPins(stepperPinList, self.StepSequence[j][0],
                                                        self.StepSequence[j][1],
                                                        self.StepSequence[j][2],
                                                        self.StepSequence[j][3])
                    time.sleep(stepDelay)
            else:
                for j in reversed(range(8)):
                    self.SetStepperMotorPins(stepperPinList, self.StepSequence[j][0],
                                                        self.StepSequence[j][1],
                                                        self.StepSequence[j][2],
                                                        self.StepSequence[j][3])
                    time.sleep(stepDelay)


    def PrimeTrack(self):
        cardWheelThread = threading.Thread(target=self.RotateStepper,
                                           args=("card wheel", 440, "counterclockwise", 0.001))
        trackThread = threading.Thread(target=self.RotateStepper,
                                           args=("track", 440, "counterclockwise", 0.001))
        cardWheelThread.start()
        trackThread.start()

        cardWheelThread.join()
        trackThread.join()

    def DealCard(self):
        cardWheelThread = threading.Thread(target=self.RotateStepper,
                                           args=("card wheel", 220, "counterclockwise", 0.001))
        trackThread = threading.Thread(target=self.RotateStepper,
                                           args=("track", 220, "counterclockwise", 0.001))
        cardWheelThread.start()
        trackThread.start()

        cardWheelThread.join()
        trackThread.join()

    def SetStepperMotorPins(self, pinArray, pin1Val, pin2Val, pin3Val, pin4Val):
        GPIO.output(pinArray[0], pin1Val)
        GPIO.output(pinArray[1], pin2Val)
        GPIO.output(pinArray[2], pin3Val)
        GPIO.output(pinArray[3], pin4Val)

    def cleanup(self):
        GPIO.output(self.ShufflerPWMPin, False)
        GPIO.output(self.ShufflerIn1Pin, False)
        GPIO.output(self.ShufflerIn2Pin, False)

        for pin in self.CardWheelStepPins:
            GPIO.output(pin, False)

        for pin in self.TrackStepPins:
            GPIO.output(pin, False)

def main():
    motorController = MotorController()
    #motorController.RotateStepper("track", 720, "counterclockwise", 0.001)
    #motorController.RotateStepper("card wheel", 360, "counterclockwise", 0.001)
    stepDelay = 0.001
    numDegrees = 220
    cardWheelThread = threading.Thread(target=motorController.RotateStepper,
                                       args=("card wheel", numDegrees, "counterclockwise", stepDelay))
    trackThread = threading.Thread(target=motorController.RotateStepper,
                                       args=("track", numDegrees, "counterclockwise", stepDelay))
    cardWheelThread.start()
    trackThread.start()

    cardWheelThread.join()
    trackThread.join()

    motorController.cleanup()

if __name__ == "__main__":
    main()
