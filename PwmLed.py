from gpiozero import PWMLED
from time import sleep


class MyPWMLED:
    """Class used for making PWM LED Objects.

    Raspberry Pi Zero W2 has enabled PWM on pins: GPIO12 & GPIO13

    :param name:        string
    :param pin_number:  int  the number of the pwm enabled pin
    :param frequency:   frequency (in Hz) Defaults to 100
    :param initial_value: Start value for the PWMLED Defaults to 1.0
    """
    def __init__(self, name: str, pin_number: int, frequency: int = 100, initial_value: float = 1.0):
        self.name = name
        self.pin_number = pin_number
        self.pin_object = PWMLED(pin_number, frequency=100)
        self.frequency = frequency
        self.value = initial_value

    def set_frequency(self, frequency: int):
        """Set function for PWMLED frequency
        :param frequency int value
        """
        self.pin_object.frequency(frequency)

    def print_demo(self):
        """prints basic infor about the Pin object"""
        print(f"Hello!\nI am {self.name}\nMy pin number is: {self.pin_number}"
              f"\n My frequency is: {self.frequency}\nMy current value is: {self.value}")

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

