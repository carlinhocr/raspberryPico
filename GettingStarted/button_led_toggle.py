import machine
import utime

button = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
led_external = machine.Pin(15, machine.Pin.OUT)

while True:
    if button.value() == 1:
        led_external.toggle()
        utime.sleep(1)