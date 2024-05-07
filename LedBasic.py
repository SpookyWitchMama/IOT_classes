from gpiozero import LED
from time import sleep


class BasicLed:
    """Class used for making basic LED Objects.

    :param name:       string
    :param pin_number: int  the number of the GPIO pin.
    """

    def __init__(self, name, pin_number):
        self.name = name
        self.pin_number = pin_number
        self.pin_object = LED(pin_number)

    def print_demo(self):
        """prints basic infor about the Pin object"""
        print(f"Hello!\nI am {self.name}\nmy pin number is: {self.pin_number}\n")

    def test_blink(self):
        """tests the LED connecting by blinking the LED for 10 sec"""
        print("I am not testing if I can blink and LED: ")
        self.pin_object.blink()
        sleep(10)
        print("did I blink?")

    def on(self):
        """Function to turn LED On"""
        self.pin_object.on()

    def off(self):
        """Function to turns LED Off"""
        self.pin_object.off()


