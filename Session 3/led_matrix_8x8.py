import spidev
import time

# ---------------- SPI SETUP ----------------
spi = spidev.SpiDev()
spi.open(0, 0)                 # Bus 0, CE0
spi.max_speed_hz = 1000000
spi.mode = 0

# ---------------- FUNCTION TO SEND DATA ----------------
def send(register, data):
    spi.xfer2([register, data])

# ---------------- MAX7219 INITIALIZATION ----------------
send(0x09, 0x00)   # Decode mode OFF
send(0x0A, 0x08)   # Brightness
send(0x0B, 0x07)   # Scan limit: 8 rows
send(0x0C, 0x01)   # Normal operation
send(0x0F, 0x00)   # Display test OFF

# ---------------- HEX PATTERN FOR LETTER "A" ----------------
A = [
    0x18,  # 00011000
    0x24,  # 00100100
    0x42,  # 01000010
    0x7E,  # 01111110
    0x42,  # 01000010
    0x42,  # 01000010
    0x42,  # 01000010
    0x00   # 00000000 (empty row)
]

# ---------------- DISPLAY THE LETTER ----------------
for row in range(8):
    send(row + 1, A[row])

# ---------------- OPTIONAL ANIMATION: FLASH EACH ROW ----------------
while True:
    for row in range(1, 9):
        send(row, 0xFF)         # Turn on all LEDs in the row
        time.sleep(0.2)
        send(row, 0x00)         # Turn off the row
    break                        # Run only once (remove break for infinite loop)

# ---------------- CLEAR LAST ROW ----------------
send(row, 0x00)
