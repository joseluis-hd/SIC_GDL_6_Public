from gpiozero import LED
from time import sleep

led = {
    "red": LED(5),
    "yellow": LED(6),
    "green": LED(13)
}

x=0

while True:
    if x > 3:
        x=0
    led[x].blink(on_time=1, off_time=1)
    sleep(2)
