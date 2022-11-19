import board
import analogio
import time
import busio
from rgb1602 import Screen

i2c = busio.I2C(board.GP9, board.GP8)
screen = Screen(i2c)
raw = analogio.AnalogIn(board.GP28)

#screen.set_css_colour("green")

while True:
	raw_voltage = raw.value * 3.3 / 65535
	
	screen.update("Raw. : {0:0.4f}V".format(raw_voltage))
	time.sleep(1.0)
