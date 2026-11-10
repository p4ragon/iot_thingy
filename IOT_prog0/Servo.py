from machine import Pin,PWM
import time

# calcoliamo il range su cui opera il servo motore 
# minima posizione (0 gradi) -> duty = durata impulso alto/periodo 0.5ms/20ms = 0.025 = 2.5% duty cycle
# massima posizione (180 gradi) -> duty = durata impulso alto/periodo 2.4ms/20ms = 0.12 = 12% duty cycle

# Risoluzione a 10 bit per duty cycle 0 e 2^10-1 (0-1023).
# 0.025*1023=25.575
# 0.12*1023=122.76


class SERVO:

    def __init__(self,pin):
    
        self.pin=pin
        self.curduty=22
        
        self.sg90 = PWM(Pin(pin, mode=Pin.OUT))
        self.sg90.freq(50)
        
        self.sg90.duty(self.curduty)
        
        
    def aggiornaServo(self, soglia, luminosita):
        
        #if luminosita>soglia+500 and self.curduty!=121:
        if luminosita>soglia-1000 and self.curduty!=121:
            
            self.sg90.duty(121)
            self.curduty=121
            
        if luminosita>soglia and self.curduty!=61:
            
            self.sg90.duty(61)
            self.curduty=61
            
        elif self.curduty!=22:
            
            self.sg90.duty(22)
            self.curduty=22
    
            
        