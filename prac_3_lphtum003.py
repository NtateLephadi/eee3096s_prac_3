from gpiozero import PWMLED, Button
import time

led = PWMLED(pin=22, active_high=True, initial_value=0, frequency=100, pin_factory=None)
on_off = Button(pin=23, pull_up=False, bounce_time=None, hold_time=1, hold_repeat=False, pin_factory=None)
bright = Button(pin=24, pull_up=False, bounce_time=None, hold_time=1, hold_repeat=False, pin_factory=None)
dim = Button(pin=25, pull_up=False, bounce_time=None, hold_time=1, hold_repeat=False, pin_factory=None)

while True:
    while(on_off.is_pressed):
        led.toggle()
        time.sleep(1)
    while(bright.is_pressed):
        if(led._read()==1.0):
            led.toggle()
        elif(led._read()==0.0):
            led._write(-0.1)            
            led.toggle()
        else:
            duty_cycle = led._read()
            duty_cycle -= 0.1
            led._write(duty_cycle)            
            led.toggle()                        
        time.sleep(1)        
    while(dim.is_pressed):
        if(led._read()==0.0):
            led.toggle()
        elif(led._read()==1.0):
            led._write(0.15)            
            led.toggle()
        else:
            duty_cycle = led._read()
            duty_cycle += 0.15
            led._write(duty_cycle)            
            led.toggle()            
        time.sleep(1)