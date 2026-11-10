from machine import Pin
import time

last_on = 0

class BUTTON:
    def __init__(self, pin):
        self.button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
    
    def mod_toggle(irq, mod):
        global last_on
    
        time_ms = time.ticks_ms() 
        delay = time.ticks_diff(time_ms, last_on) 
        if (delay < 200): # Se la differenza è inferiore a 200ms (tempo di debounce), ignora l'input.
            return
    
        last_on = time_ms
    
        mod = (mod + 1) % 2
        return mod
    
    