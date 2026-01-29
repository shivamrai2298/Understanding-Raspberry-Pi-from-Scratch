In Bash
sudo raspi-config

Enale Camera
Interface Options → Camera → Enable

Reboot
sudo reboot

Verify
libcamera-hello


Capture photo
libcamera-still -o image.jpg

with 5 sec delay
libcamera-still -t 5000 -o image.jpg

