from Photoresistor import PHOTORESISTOR
from Buzzer import BUZZER
from LED_5000hz import LED_5000hz
from stepmotor import STEPMOTOR
from button import BUTTON
from potenziometer import POTENZIOMETER
from Servo import SERVO
from time import sleep
import time
from machine import Pin,PWM,ADC




btn=BUTTON(17)
buzzer=BUZZER(16)
stepmotor=STEPMOTOR(33,25,26,27)
servo=SERVO(18)
ldr=PHOTORESISTOR(32)
ptn=POTENZIOMETER(34)
led=LED_5000hz(14)

btn.button.irq(trigger=Pin.IRQ_RISING, handler=btn._mod_toggle)

buzzer.suono_avvio()


vmin=1000
vmax=3000



while True:
    if btn.mod==False:
        lum=ldr.read()
        soglia=int(vmin+(vmax-vmin)*(ptn.read()/4095))
        print("Luminosità rilevata: ",lum)
        print("Soglia impostata a: ",soglia)
        led.update(soglia,lum)
        servo.aggiornaServo(soglia,lum)
        if lum<soglia:
            stepmotor.single_step(-1)
        else:
            stepmotor.single_step(+1)
        sleep(1)
    else:
        servo.aggiornaServo(0,10000)
        stepmotor.half_step(-1)
        #x=ptn.read()/4095*1023
        led.set_duty_raw(int(ptn.read()/4095*1023))
        
        
        
    
    
    
    
