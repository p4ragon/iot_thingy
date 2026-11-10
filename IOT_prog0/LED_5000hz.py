from machine import Pin, PWM,ADC
import time
class LED_5000hz:
    def __init__(self, pin, freq=5000):
        self.pwm = PWM(Pin(pin, mode=Pin.OUT), freq=freq)
        
        
    #funzione per impostare il duty cycle
    def set_duty_raw(self, duty_value):
        self.pwm.duty(duty_value)
        
    #funzione per convertire una percentuale -> range 2^10-1=1023
    #funzione di sostegno per la update 
    def set_percentage(self, percentage):
        val=int((percentage/100)*1023)
        self.set_duty_raw(val)
        
    #logica di gestione luminosità led
    def update(self, soglia, luminosita):
        """
        Calcola la differenza (soglia - luminosita) e imposta
        il duty cycle corrispondente alle specifiche.
        """
        diff = soglia - luminosita

        if diff > 800:
            duty_percent = 100
        elif 400 <= diff <= 800:
            duty_percent = 70
        elif 100 <= diff <= 399:
            duty_percent = 30
        else:
            # Luminosità uguale/superiore alla soglia (diff <= 0) o scarto < 100
            duty_percent = 0

        self.set_percentage(duty_percent)
        return duty_percent
    
    