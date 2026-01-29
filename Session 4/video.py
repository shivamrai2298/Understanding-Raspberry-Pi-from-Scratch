from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(bitrate=10000000)
output = FileOutput("video.h264")

picam2.start_recording(encoder, output)
time.sleep(10)   # record 10 seconds
picam2.stop_recording()
