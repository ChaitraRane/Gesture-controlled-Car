# Gesture-controlled-Car

## Overview
This project enables a car to be controlled using hand gestures detected via a webcam. The system interprets finger movements and sends commands to an Arduino, which controls the car's motion using an L298N motor driver. This touchless control system is useful for robotics applications and smart automation.

## Features
- Uses a webcam to detect hand gestures.
- Controls a car’s movement (forward, backward, left, and right) via an Arduino and an L298N motor driver.
- Real-time gesture recognition with OpenCV and CVZone.

## Hardware Requirements
- Arduino board
- L298N Motor Driver
- 2 DC Motors (for driving wheels)
- 2 Additional Wheels (for support)
- Webcam
- Computer with Python installed

## Software Requirements
- Python 3.x
- OpenCV (`cv2`)
- CVZone (`cvzone`)
- PyFirmata (`pyfirmata`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Gesture-Controlled-Car.git
   cd Gesture-Controlled-Car
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python cvzone pyfirmata
   ```
3. Connect the Arduino and modify `controller.py` to match the correct COM port.

## Usage
1. Run the script:
   ```sh
   python main.py
   ```
2. Use the following hand gestures to control the car:
   - No fingers up: Stop the car
   - Index finger up: Turn right
   - Index and middle finger up: Turn left
   - Three fingers up: Move forward
   - Four fingers up: Move backward
   - All fingers up: Move at full speed
3. Press 'k' to exit.

## Files
- `main.py`: Handles hand detection and gesture recognition.
- `controller.py`: Controls the car's motors based on recognized gestures.



