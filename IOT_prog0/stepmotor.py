import utime
from machine import Pin

class STEPMOTOR:
    # Definisco i pin per stepper motor
    def __init__(pin1, pin2, pin3, pin4):
        self.IN1=Pin(pin1, Pin.OUT)
        self.IN2=Pin(pin2, Pin.OUT)
        self.IN3=Pin(pin3, Pin.OUT)
        self.IN4=Pin(pin4, Pin.OUT)

    stepper_pins = [self.IN1, self.IN2, self.IN3, self.IN4]

    
    step_sequence = [
        [1, 0, 0, 1],  
        [1, 1, 0, 0],  
        [0, 1, 1, 0],  
        [0, 0, 1, 1],  
    ]

    step_sequence_half = [
        [1,0,0,0],  # solo IN1
        [1,0,0,1],  # IN1+IN4
        [0,0,0,1],  # solo IN4
        [0,0,1,1],  # IN3+IN4
        [0,0,1,0],  # solo IN3
        [0,1,1,0],  # IN2+IN3
        [0,1,0,0],  # solo IN2
        [1,1,0,0],  # IN1+IN2
    ]

    step_index = 0

#direction = +1 (antiorario), -1 (orario)
#steps = numero di passi da eseguire
#delay = tempo tra un passo e l'altro
#step_index tiene traccia della posizione corrente nella sequenza di attivazione (fase) del motore.

    def step(direction, steps, delay):
        global step_index 
        for i in range(steps):
            # l'operatore % garantisce che step_index rimanga all'interno dell'intervallo valido,
            # assicurando che la sequenza dei passi venga ripetuta ciclicamente.
            # indica la riga quindi quale passo
            step_index = (step_index + direction) % len(step_sequence)
        
        
            #pin_index determina la colonna (quindi la bobbina)
            for pin_index in range(len(stepper_pins)):
                 pin_value = step_sequence[step_index][pin_index]
                stepper_pins[pin_index].value(pin_value)
        
        
            utime.sleep(delay)
