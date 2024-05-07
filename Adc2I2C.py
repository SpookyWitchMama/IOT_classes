import smbus


class A2DSensor:
    """Class for Analog to I2C conversion

    :param name:        Name of the sensor
    :param address:     Hexadecimal address of the I2C bus
    :param bus_number:  Group of GPIO the sensor is connected to. Raspberry Pi Zero 2 has bus group on GPIO
    """
    def __init__(self, name: str, address: int = 0x00, bus_number: int = 1):
        self.name = name
        self.address = address
        self.bus_number = bus_number
        self.i2c_bus = smbus.SMBus(bus_number)

    def read_analog(self):
        """Function for reading I2C with SMBus.

        Reads from A2DSensor class SMBus object and returns 2 bytes as integer.

        2 bytes = 16 bit

        :return:  Returns word as a INT
        """
        word = self.i2c_bus.read_word_data(self.address, 0)
        return word

    def i2cbitswitch2pie0(self, word=read_analog()):
        """Function that calls read_analog() and returns the bytes bitshifted

        :return: INT
        """
        first = (word & 0xff) << 8      # or 0b0000000011111111
        second = (word & 0xff00) >> 8   # or 0b1111111100000000
        data = first | second           # bitwise OR
        return data

# Word is sample of 2bytes = 16 bits
# word = 0xabff
# print(bin(word))

# Bitwise AND before Bit-shifting 8 places
# first = (word & 0b0000000011111111) << 8   # or 0xff
# second = (word & 0b1111111100000000) >> 8  # or 0xff00
# data = first | second   # bitwise OR

# print(bin(data))

# f string print example.
# print(f'{word:016b}')
# rint(f'{first:016b}')
# print(f'{second:016b}')
# print(f'{data:016b}')
