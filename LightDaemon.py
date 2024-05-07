import schedule
import time
import pigpio


class LightDemon:
    def __init__(self, start_time, stop_time, gpio_pin):
        self.start_time = start_time
        self.stop_time = stop_time
        self.duty = None
        self.gpio_pin = gpio_pin
        self.pi = pigpio.pi()
        self.pi.set_PWM_range(self.gpio_pin, 100)

    def init_schedule(self):
        schedule.every().day.at(self.start_time).do(self.on)
        schedule.every().day.at(self.stop_time).do(self.off)

    def on(self):
        self.pi.set_PWM_dutycycle(self.gpio_pin, 50)

    def off(self):
        self.pi.set_PWM_dutycycle(self.gpio_pin, 0)


if __name__ == "__main__":

    lamp = LightDemon('10:30','12:30', 13)
    lamp.init_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)
