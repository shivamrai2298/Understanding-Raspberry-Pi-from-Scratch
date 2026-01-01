# ====================================================
# Experiment Title:
# LED Dimming using PWM on Raspberry Pi
#

# ====================================================
# OBJECTIVE:
# To control the brightness of an LED using
# Pulse Width Modulation (PWM).
# ====================================================

# ================== QUESTIONS ==================

# Q1. What is PWM?
# Ans:
# PWM (Pulse Width Modulation) is a technique used
# to simulate analog output using digital signals
# by rapidly switching the signal ON and OFF.

# Q2. Why PWM is required for LED dimming?
# Ans:
# Raspberry Pi GPIO pins provide only digital output
# (HIGH or LOW). PWM allows us to control LED
# brightness by varying ON-time.

# Q3. What is duty cycle?
# Ans:
# Duty cycle is the percentage of time the signal
# remains HIGH in one PWM cycle.

# Q4. What happens if duty cycle is 100%?
# Ans:
# The LED remains fully ON at maximum brightness.

# Q5. What happens if duty cycle is 0%?
# Ans:
# The LED remains OFF.

# Q6. What is PWM frequency?
# Ans:
# PWM frequency is the number of ON-OFF cycles
# per second. It is measured in Hertz (Hz).

# Q7. Why is GPIO.cleanup() important?
# Ans:
# It resets GPIO pins to a safe state and prevents
# hardware conflicts.

# ====================================================
# PROGRAM CODE
# ====================================================

import RPi.GPIO as GPIO   # GPIO control library
import time              # Time delay library

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# GPIO pin connected to LED
LED_PIN = 18

# Set LED pin as OUTPUT
GPIO.setup(LED_PIN, GPIO.OUT)

# Create PWM object on LED pin with frequency 100Hz
pwm = GPIO.PWM(LED_PIN, 100)

# Start PWM with 0% duty cycle (LED OFF)
pwm.start(0)

try:
    # Gradually increase brightness
    for duty in range(0, 101, 5):
        pwm.ChangeDutyCycle(duty)
        print(f"Brightness: {duty}%")
        time.sleep(0.1)

    # Gradually decrease brightness
    for duty in range(100, -1, -5):
        pwm.ChangeDutyCycle(duty)
        print(f"Brightness: {duty}%")
        time.sleep(0.1)

# Stop execution safely on Ctrl+C
except KeyboardInterrupt:
    print("Program interrupted by user")

# Cleanup GPIO before exiting
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO cleanup completed")


