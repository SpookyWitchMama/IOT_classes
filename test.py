import LedBasic
import PwmLed
import WaterDaemon

"""
hello = PwmLed.MyPWMLED("myLed", 12)
test_pin = LedBasic.BasicLed("test pin", 5)
test_pin.print_demo()
led1 = PwmLed.MyPWMLED("myled", 15)

test_pin.on()
test_pin.off()
"""

pump = WaterDaemon.WaterDemon('pump1', 12)

pump.pump_water(5)

