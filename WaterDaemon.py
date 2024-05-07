import pigpio
from time import sleep


class WaterDemon:
    def __init__(self, name: str, gpio_pin: int):
        self.name = name
        self.duty = None
        self.gpio_pin = gpio_pin
        self.pi = pigpio.pi('192.168.34.33', 8888)
        self.pi.set_PWM_range(self.gpio_pin, 100)

    def pump_on(self):
        self.pi.set_PWM_dutycycle(self.gpio_pin, 50)
        print("pump is on")

    def pump_off(self):
        self.pi.set_PWM_dutycycle(self.gpio_pin, 0)
        print("pump is off")

    def pump_water(self, time_in_sec: int):
        self.pump_on()
        sleep(time_in_sec)
        self.pump_off()

