sudo apt update
sudo apt install python3-picamera2 -y

from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.start()

time.sleep(2)  # camera warm-up
picam2.capture_file("photo.jpg")

picam2.stop()
