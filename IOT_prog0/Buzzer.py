from machine import Pin, PWM
from time import sleep_ms

class BUZZER:
    def __init__(self, sig_pin):
        # Inizializza PWM con frequenza base e duty 0 (spento)
        self.pwm = PWM(Pin(sig_pin, Pin.OUT), freq=1000, duty=0)

    # 1 beep, 1000Hz, 200ms; 2 beep, 1500Hz, 100ms (AUTO); 1 beep, 2000Hz, 300ms (MANUAL)
    # 3 beep, 800Hz, 150ms (Low light alarm)
    def beep(self, freq, durata, duty=512):
        self.pwm.freq(freq)
        self.pwm.duty(duty)
        sleep_ms(durata)      # Usa direttamente sleep_ms
        self.stop()

    def suono_avvio(self):
        self.beep(freq=1000, durata=200)

    def suono_auto(self):
        self.beep(freq=1500, durata=100)
        sleep_ms(100)
        self.beep(freq=1500, durata=100)
        sleep_ms(100)

    def suono_manuale(self):
        self.beep(freq=2000, durata=300)

    def allarme(self):
        for _ in range(3):
            self.beep(freq=800, durata=150)
            sleep_ms(100)

    def stop(self):
        self.pwm.duty(0)