# Motion Sensor Arduino Project

A simple Arduino project that detects motion using a tilt/movement sensor and lights up an LED when motion is detected.

## Description

This Arduino sketch monitors a digital input pin connected to a motion sensor (such as a tilt switch, ball switch, or vibration sensor). When movement is detected, an LED lights up for a short period of time, providing visual feedback.

The project works by:
1. Reading the current state of the sensor
2. Detecting changes in the sensor's state
3. Turning on an LED when motion is detected
4. Automatically turning off the LED after a short delay

## Hardware Requirements

* Arduino board (Uno, Nano, etc.)
* Motion/tilt sensor (connected to pin 2)
* LED (connected to pin 5)
* 220-330 ohm resistor for the LED
* Jumper wires
* Breadboard (optional)

## Circuit Connection

1. Connect the motion sensor to digital pin 2 (with internal pull-up resistor enabled)
2. Connect the LED to digital pin 5 through a current-limiting resistor
3. Connect appropriate power (5V) and ground connections

## Installation

1. Clone this repository or download the `spectacular_rottis_gogo1.ino` file
2. Open the file in the Arduino IDE
3. Connect your Arduino board to your computer
4. Select the correct board and port from the Tools menu
5. Upload the sketch to your Arduino

## Configuration

You can adjust the sensitivity and behavior by modifying these variables:
- `shaketime`: Duration in milliseconds that the LED stays on after motion is detected (default: 50ms)

## How It Works

- The code uses Arduino's internal pull-up resistor for the motion sensor input
- When the sensor detects motion, it changes its state
- The program detects this change and records the time
- The LED turns on whenever motion is detected within the last `shaketime` milliseconds

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

Credit - [Sumit Kudalkar](https://www.linkedin.com/in/sumit-kudalkar-7ab0a1321?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)