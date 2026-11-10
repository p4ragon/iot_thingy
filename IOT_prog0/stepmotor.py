import utime
from machine import Pin

class STEPMOTOR:
    # Sequenze di attivazione dei passi
    step_sequence = [
        [1, 0, 0, 1],  
        [1, 1, 0, 0],  
        [0, 1, 1, 0],  
        [0, 0, 1, 1],  
    ]

    step_sequence_half = [
        [1, 0, 0, 0],  # solo IN1
        [1, 0, 0, 1],  # IN1+IN4
        [0, 0, 0, 1],  # solo IN4
        [0, 0, 1, 1],  # IN3+IN4
        [0, 0, 1, 0],  # solo IN3
        [0, 1, 1, 0],  # IN2+IN3
        [0, 1, 0, 0],  # solo IN2
        [1, 1, 0, 0],  # IN1+IN2
    ]

    def __init__(self, pin1, pin2, pin3, pin4):
        self.IN1 = Pin(pin1, Pin.OUT)
        self.IN2 = Pin(pin2, Pin.OUT)
        self.IN3 = Pin(pin3, Pin.OUT)
        self.IN4 = Pin(pin4, Pin.OUT)

        # Inizializzati dentro __init__ dove self esiste
        self.stepper_pins = [self.IN1, self.IN2, self.IN3, self.IN4]
        self.step_index = 0
        self.sequence = self.step_sequence_half
        
    def single_step(self, direction, delay=0.002):
        """Esegue esattamente un singolo passo/semipasso."""
        self.step_index = (self.step_index + direction) % len(self.sequence)
        
        for pin_index, pin in enumerate(self.stepper_pins):
            pin.value(self.sequence[self.step_index][pin_index])
            
        utime.sleep(delay)

    def step(self, direction, delay=0.002, steps=1):
        """Esegue N passi (default: 1 singolo passo)."""
        for _ in range(steps):
            self.single_step(direction, delay)
            
    def step(self, direction, delay=0.005, steps=512):
        
        for _ in range(steps):
            # Aggiorna l'indice ciclicamente
            self.step_index = (self.step_index + direction) % len(self.step_sequence)
            
            # Imposta lo stato di ciascun pin per il passo corrente
            for pin_index in range(len(self.stepper_pins)):
                pin_value = self.step_sequence_half[self.step_index][pin_index]
                self.stepper_pins[pin_index].value(pin_value)
            
            utime.sleep(delay)
    def half_step(self, direction, delay=0.005, steps=256):
        
        for _ in range(steps):
            # Aggiorna l'indice ciclicamente
            self.step_index = (self.step_index + direction) % len(self.step_sequence)
            
            # Imposta lo stato di ciascun pin per il passo corrente
            for pin_index in range(len(self.stepper_pins)):
                pin_value = self.step_sequence_half[self.step_index][pin_index]
                self.stepper_pins[pin_index].value(pin_value)
            
            utime.sleep(delay)

    def stop(self):
        """Spegne tutte le bobine per evitare che il motore scaldi a riposo"""
        for pin in self.stepper_pins:
            pin.value(0)