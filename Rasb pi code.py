from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time

trig=OutputDevice(4)
echo=InputDevice(17)
motor=PWMOutputDevice(15)
sleep(2)

def get_pulse_time():
    trig.on()
    sleep(0.00001)
    trig.off()
    
    while echo.is_active == False:
        #time value when starting the UDS pulse
        pulse_start = time()
    while echo.is_active == True:
        #time value when ending the UDS pulse
        pulse_end = time()

    sleep(0.06)

    try:
        return pulse_end - pulse_start
    except:
        #if either value wasn't recorded correctly
        return 0.02

def calculate_distance(duration):
    speed=343
    #using the speed distance time triangle but dividing by two as the pulse covers the distance to and from the object
    distance=speed*duration/2
    return distance

def calculate_vibration(distance):
    #scaling the distance down to a value between 0 and 1 for the PWM input
    vibration(((distance-0.02)*-1)/(2-0.02))+1
    return vibration

while True:
    duration=get_pulse_time()
    distance=calculate_distance(duration)
    vibration=calculate_vibration(distance)
    try:
        motor.value=vibration
    except:
        #for if a distance is less than 2cm or greater than 2m leading to an invalid vibration value
        pass

