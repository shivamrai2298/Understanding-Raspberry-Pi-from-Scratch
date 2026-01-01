# ====================================================
# Experiment Title:
# Blinking an LED using Raspberry Pi and Python
#
# File Name:
# led_blink_with_questions.py
#
# ====================================================
# OBJECTIVE:
# To blink an LED connected to Raspberry Pi using
# Python programming and GPIO pins.
#
# ====================================================
# THEORY / VIVA QUESTIONS WITH ANSWERS
# ====================================================

# Q1. What is Raspberry Pi?
# Ans:
# Raspberry Pi is a low-cost, single-board computer
# that runs a Linux operating system and is used for
# learning programming, electronics, and IoT.

# Q2. What is GPIO?
# Ans:
# GPIO stands for General Purpose Input Output.
# GPIO pins allow Raspberry Pi to interact with
# external hardware like LEDs, sensors, and motors.

# Q3. Why do we use GPIO pins?
# Ans:
# GPIO pins are used to send output signals to devices
# like LEDs and to read input signals from devices
# like buttons and sensors.

# Q4. What is the role of Python in this experiment?
# Ans:
# Python is used to write a program that controls
# the GPIO pins of Raspberry Pi to turn the LED ON
# and OFF.

# Q5. Why is a resistor used with an LED?
# Ans:
# A resistor limits the current flowing through the LED
# and protects both the LED and Raspberry Pi GPIO pin
# from damage.

# Q6. What does GPIO.HIGH mean?
# Ans:
# GPIO.HIGH sends 3.3V to the GPIO pin, which turns
# the LED ON.

# Q7. What does GPIO.LOW mean?
# Ans:
# GPIO.LOW sends 0V to the GPIO pin, which turns
# the LED OFF.

# Q8. What is GPIO.setmode(GPIO.BCM)?
# Ans:
# It sets the GPIO pin numbering mode to BCM,
# which refers to the GPIO number printed on
# Raspberry Pi, not the physical pin number.

# Q9. What does time.sleep() do?
# Ans:
# time.sleep() pauses the program execution for
# a specified number of seconds.

# Q10. Why is GPIO.cleanup() important?
# Ans:
# GPIO.cleanup() resets the GPIO pins to a safe state
# and prevents hardware conflicts after the program
# stops.

# ====================================================
# PROGRAM CODE
# ====================================================

# Import GPIO library to control Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Import time library to create delays
import time

# Set GPIO numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pin number where LED is connected
LED_PIN = 18

# Set LED pin as OUTPUT
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Infinite loop to blink LED continuously
    while True:
        # Turn LED ON
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # Wait for 1 second

        # Turn LED OFF
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # Wait for 1 second

# Stop program safely when Ctrl + C is pressed
except KeyboardInterrupt:
    print("Program interrupted by user")

# Cleanup GPIO pins before exiting
finally:
    GPIO.cleanup()
    print("GPIO cleanup completed")

# ====================================================
