"""Simple test script for 2.9" 296x128 black and white display.

Supported products:
  * Adafruit Flexible 2.9" Black and White
    * https://www.adafruit.com/product/4262
  """

import time
import board
import busio
import displayio
import adafruit_il0373

displayio.release_displays()

# This pinout works on a Metro and may need to be altered for other boards.

# For breadboarding
spi = busio.SPI(board.SCL, board.SDA)
epd_cs = board.D9
epd_dc = board.D8
epd_reset = board.D7
epd_busy = board.D6

display_bus = displayio.FourWire(spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset,
                                 baudrate=1000000)
time.sleep(1)

display = adafruit_il0373.IL0373(display_bus, width=296, height=128, rotation=90, busy_pin=epd_busy, swap_rams=True)

g = displayio.Group()

f = open("/display-ruler.bmp", "rb")

pic = displayio.OnDiskBitmap(f)
t = displayio.TileGrid(pic, pixel_shader=displayio.ColorConverter())
g.append(t)

display.show(g)

display.refresh()

time.sleep(120)
