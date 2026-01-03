# ---------------------------------------------------------
# Experiment: Stepper Motor Control using Raspberry Pi
# Motor Type: 28BYJ-48 with ULN2003 Driver
# Language: Python
# ---------------------------------------------------------

"""
==============================
THEORY / VIVA QUESTIONS & ANSWERS
==============================

Q1. What is a stepper motor?
A: A stepper motor is a brushless DC motor that rotates in
   discrete steps instead of continuous rotation.

Q2. Why do we use a driver (ULN2003)?
A: Raspberry Pi GPIO pins cannot supply enough current.
   The driver amplifies current and protects the GPIO pins.

Q3. What is a step angle?
A: The angle moved by the motor in one step.
   Example: 28BYJ-48 has 5.625° with gear reduction.

Q4. Difference between DC motor and stepper motor?
A:
- DC motor rotates continuously
- Stepper motor rotates step-by-step with high precision

Q5. Where are stepper motors used?
A:
- CNC machines
- 3D printers
- Robotics
- Camera sliders
- Industrial automation

Q6. What happens if sequence is wrong?
A: Motor will vibrate or rotate incorrectly.

==============================
"""

# ---------------------------------------------------------
# Import required libraries
# ---------------------------------------------------------
import RPi.GPIO as GPIO
import time

# ---------------------------------------------------------
# GPIO SETUP
# ---------------------------------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO pins connected to ULN2003 IN1-IN4
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

control_pins = [IN1, IN2, IN3, IN4]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# ---------------------------------------------------------
# Stepper motor step sequence (Half-step mode)
# ---------------------------------------------------------
half_step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

# ---------------------------------------------------------
# MAIN LOGIC
# ---------------------------------------------------------
try:
    print("Stepper Motor Rotating Clockwise")

    # Rotate motor 512 steps (~1 full rotation for 28BYJ-48)
    for step in range(512):
        for half_step in half_step_sequence:
            for pin in range(4):
                GPIO.output(control_pins[pin], half_step[pin])
            time.sleep(0.002)

    print("Rotation Completed")

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up")
