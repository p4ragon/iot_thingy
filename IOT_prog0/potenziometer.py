from machine import Pin, ADC
import time

class POTENZIOMETER:
    def __init__(self,pin):
        self.adc = ADC(Pin(pin, mode=Pin.IN))
        self.adc.atten(ADC.ATTN_11DB)    # Misura 0-3.3V
    
    def read(self):
        return self.adc.read()
        
    
