import pyfirmata

# Set the COM port for Arduino
comport = 'COM6'  # Replace with your Arduino's COM port.
board = pyfirmata.Arduino(comport)

# Define motor control pins (L298N connections)
in1 = board.get_pin('d:6:o')  # IN1 for Motor A (left/right control)
in2 = board.get_pin('d:9:o')  # IN2 for Motor A (left/right control)
ena = board.get_pin('d:10:p')  # ENA for Motor A (PWM control)

in3 = board.get_pin('d:11:o')  # IN3 for Motor B (forward/backward control)
in4 = board.get_pin('d:12:o')  # IN4 for Motor B (forward/backward control)
enb = board.get_pin('d:3:p')   # ENB for Motor B (PWM control)

def control_motor(fingerUp):
    """
    Controls Motor A (left/right) and Motor B (forward/backward) using the fingerUp input.
    """
    # All fingers down: Stop both motors
    if fingerUp == [0, 0, 0, 0, 0]:
        # Stop both motors
        in1.write(0)
        in2.write(0)
        ena.write(0)  # Set speed to 0 (stop Motor A)
        in3.write(0)
        in4.write(0)
        enb.write(0)  # Set speed to 0 (stop Motor B)

    # Index finger up: Turn right (Motor A moves forward)
    elif fingerUp == [0, 1, 0, 0, 0]:
        # Motor A turns right
        in1.write(1)
        in2.write(0)
        ena.write(0.5)  # Adjust speed for Motor A (right)

        # Stop Motor B
        in3.write(0)
        in4.write(0)
        enb.write(0)

    # Index and middle finger up: Turn left (Motor A moves backward)
    elif fingerUp == [0, 1, 1, 0, 0]:
        # Motor A turns left
        in1.write(0)
        in2.write(1)
        ena.write(0.5)  # Adjust speed for Motor A (left)

        # Stop Motor B
        in3.write(0)
        in4.write(0)
        enb.write(0)

    # Three fingers up: Move forward (Motor B moves forward)
    elif fingerUp == [0, 1, 1, 1, 0]:
        # Motor B moves forward
        in3.write(1)
        in4.write(0)
        enb.write(0.5)  # Adjust speed for Motor B (forward)

        # Stop Motor A
        in1.write(0)
        in2.write(0)
        ena.write(0)

    # Four fingers up: Move backward (Motor B moves backward)
    elif fingerUp == [0, 1, 1, 1, 1]:
        # Motor B moves backward
        in3.write(0)
        in4.write(1)
        enb.write(0.5)  # Adjust speed for Motor B (backward)

        # Stop Motor A
        in1.write(0)
        in2.write(0)
        ena.write(0)

    # All fingers up: Move both motors at full speed
    elif fingerUp == [1, 1, 1, 1, 1]:
        # Motor A moves forward (right), Motor B moves forward
        in1.write(1)
        in2.write(0)
        ena.write(0.5)  # Full speed for Motor A

        in3.write(0)
        in4.write(1)
        enb.write(0.5)  # Full speed for Motor B
