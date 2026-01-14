# ---------------------------------------------------------
# Experiment: 8x8 LED Matrix using MAX7219 and Raspberry Pi
# Interface: SPI
# ---------------------------------------------------------

"""
==============================
VIVA / THEORY QUESTIONS
==============================

Q1. What is an 8x8 LED matrix?
A: A display consisting of 64 LEDs arranged in rows and columns.

Q2. Why do we use MAX7219?
A: Raspberry Pi GPIO cannot handle 64 LEDs.
   MAX7219 handles current, multiplexing, and SPI communication.

Q3. What is multiplexing?
A: Turning rows ON and OFF very fast to display patterns.

Q4. Why SPI is used?
A: SPI allows fast communication using fewer pins.

Q5. Can we connect LED matrix directly to GPIO?
A: No, it will damage GPIO due to high current draw.

==============================
"""

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
import time

# SPI configuration
serial = spi(port=0, device=0, gpio=noop())

# MAX7219 device setup
device = max7219(
    serial,
    cascaded=1,
    block_orientation=90,
    rotate=0
)

print("8x8 LED Matrix Started")

try:
    while True:
        with canvas(device) as draw:
            draw.text((1, 0), "Hi", fill="white")
        time.sleep(1)

        with canvas(device) as draw:
            draw.point((3, 3), fill="white")
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped")



#library Requirements

sudo apt update
sudo apt install python3-pip
pip3 install luma.led_matrix
