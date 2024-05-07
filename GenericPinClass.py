import gpiozero


class GenericOutputPin:
    def __init__(self, name: str, pin_number: int):
        """Generic class for output pins

        Creates a Pin object that which is able to send output to device

        :param name: string - name of the Pin
        :param pin_number: int - GPIO number

        """
        self.name = name
        self.pin_number = pin_number
        self.pin = gpiozero.DigitalOutputDevice(self.pin_number)

    def on(self):
        self.pin.on()

    def off(self):
        self.pin.off()

