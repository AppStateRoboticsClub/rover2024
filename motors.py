import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # use broadcom pin numbering (not board pin numbering)

# setup
# motor control pins
motorL = 13 # GPIO Pin for motorL # previously motor1
motorR = 12 # GPIO Pin for motorR # previously motor2
GPIO.setup(motorL, GPIO.OUT) # set pin motorL to output
GPIO.setup(motorR, GPIO.OUT) # set pin motorR to output

# reverse control pins
reverseL = 5 # pin for reverse left
reverseR = 6 # pin for reverse right
GPIO.setup(reverseL, GPIO.OUT) # set pin reverseL to output
GPIO.setup(reverseR, GPIO.OUT) # set pin reverseR to output
GPIO.output(reverseL, False) # set so no pin output, aka go forwards
GPIO.output(reverseR, False) # set so no pin output, aka go forwards

motorLServo = GPIO.PWM(motorL, 1000) # set Motors to PWM. Change this depeneding on how your motor controller works
motorLServo.start(8)
motorRServo = GPIO.PWM(motorR, 1000) # set Motors to PWM. Change this depeneding on how your motor controller works
motorRServo.start(8)
motorLServo.ChangeDutyCycle(0) # 
motorRServo.ChangeDutyCycle(0) # RPI can encounter a bug that might require this to be applied twice
dutyL = 5
dutyR = 5

isReversed = False

def turn(value): 
    motorLServo.ChangeDutyCycle(speed * (1 + value)) # 50 Right, 0 Neutral, -50 Left
    motorRServo.ChangeDutyCycle(speed * (1 - value))
    dutyL = 50 + value
    dutyR = 50 - value
    
def acc(value):
    # check for is reversed
    
    # reduce reverse speed
    if isReversed:
        value = value / 5

    # update pwm duty cycle to new value
    motorLServo.ChangeDutyCycle(value)
    motorRServo.ChangeDutyCycle(value)
    dutyL = value
    dutyR = value

    # update the speed
    global speed
    speed = value

def stop():
    motorLServo.stop()
    motorRServo.stop()
    
def start():
    motorLServo.start(dutyL)
    motorRServo.start(dutyR)
    
def Left(value: int):
    motorLServo.ChangeFrequency(value)
    
def Right(value: int):
    motorRServo.ChangeFrequency(value)

def setReverse(isRev: bool):
    '''
    - Takes a boolean value as a parameter as to whether the rover should be reversed, then updates
    the reverse pins to be on if reverse is true, and off if false
    - @param isRev: bool - The current state of the reverse button
    '''
    global isReversed
    if isReversed == isRev:
        return
    isReversed = isRev
    GPIO.output(reverseL, isRev)
    GPIO.output(reverseR, isRev)