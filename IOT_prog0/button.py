from machine import Pin
import time

class BUTTON:
    def __init__(self, pin):
        self.button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        self.last_press = 0
        self.mod=False # 0: Automatico, 1: Manuale 
        
    
    def _mod_toggle(self,pin):
        """Handler ISR chiamato automaticamente dall'hardware su IRQ_RISING"""
        now = time.ticks_ms()
        if time.ticks_diff(now, self.last_press) < 200:
            return  # Debounce: ignora rimbalzi sotto i 200ms
        self.last_press = now
        #si parte con modalità automatica.
        self.mod= not self.mod
        if self.mod:
            print("Modalità manuale.")
        else:
            print("Modalità automatica.")

    def get_mode(self):
        """Metodo per leggere la modalità corrente nel ciclo principale"""
        return self.mod
