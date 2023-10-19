from gpiozero import LED
from time import sleep

led_pins = {
    "green": 13,
    "yellow": 6,
    "red": 5
}

leds = {color: LED(pin) for color, pin in led_pins.items()}

while True:
    leds["green"].on()
    sleep(1)  
    leds["green"].off()

    leds["yellow"].on()
    sleep(1)  
    leds["yellow"].off()

    leds["red"].on()
    sleep(1)  
    leds["red"].off()
