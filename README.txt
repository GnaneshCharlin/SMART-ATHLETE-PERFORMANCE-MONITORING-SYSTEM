# ESP32 Health Monitoring System with Blynk Integration

This project demonstrates how to use an ESP32 development board to monitor vital health parameters like Heart Rate and Body Temperature using sensors such as the MAX30100 heart rate sensor and DHT11 temperature sensor. The readings are then sent to the Blynk platform for real-time monitoring and alert notifications.

## Purpose

The primary goal of this project is to provide a simple health monitoring solution, particularly for gym-goers or fitness enthusiasts. By monitoring heart rate and temperature during exercise, users can receive real-time feedback to avoid overexertion and potential health risks.

- Heart Rate: Monitored using the MAX30100 sensor.
- Body Temperature: Measured using the DHT11 sensor.

## Features

- Real-time Health Data: Continuously reads heart rate and temperature from the sensors.
- Blynk Integration: Sends data to the Blynk app for remote monitoring.
- Alerts: Sends notifications when heart rate exceeds 120 bpm or when body temperature exceeds 37.5°C.
- IoT-based System: Data is transmitted over Wi-Fi, making it ideal for remote health monitoring.

## Components

- ESP32 Development Board
- MAX30100 Heart Rate and SpO2 Sensor
- DHT11 Temperature and Humidity Sensor
- Blynk App (for monitoring data)
- Jumper Wires
- Breadboard (optional, for prototyping)

## Software Tools

- MicroPython: The main programming environment for the ESP32.
- Thonny or uPyCraft IDE: Used to write and upload code to the ESP32.
- Blynk App: Used to visualize sensor data and receive alerts.
- Python: The requests library is used to send data to the Blynk API.
- uRequests (MicroPython): A MicroPython version of the `requests` library to send data to Blynk.

## Wiring Diagram

- DHT11 Temperature Sensor:
  - VCC → 3.3V on ESP32
  - GND → GND on ESP32
  - DATA → GPIO 4 on ESP32

- MAX30100 Heart Rate Sensor:
  - VCC → 3.3V on ESP32
  - GND → GND on ESP32
  - SDA → GPIO 21 on ESP32
  - SCL → GPIO 22 on ESP32

## Installation

# ESP32 Health Monitoring System with Blynk Integration

This project demonstrates how to use an ESP32 development board to monitor vital health parameters like Heart Rate and Body Temperature using sensors such as the MAX30100 heart rate sensor and DHT11 temperature sensor. The readings are then sent to the Blynk platform for real-time monitoring and alert notifications.

## Purpose

The primary goal of this project is to provide a simple health monitoring solution, particularly for gym-goers or fitness enthusiasts. By monitoring heart rate and temperature during exercise, users can receive real-time feedback to avoid overexertion and potential health risks.

- Heart Rate: Monitored using the MAX30100 sensor.
- Body Temperature: Measured using the DHT11 sensor.

## Features

- Real-time Health Data: Continuously reads heart rate and temperature from the sensors.
- Blynk Integration: Sends data to the Blynk app for remote monitoring.
- Alerts: Sends notifications when heart rate exceeds 120 bpm or when body temperature exceeds 37.5°C.
- IoT-based System: Data is transmitted over Wi-Fi, making it ideal for remote health monitoring.

## Components

- ESP32 Development Board
- MAX30100 Heart Rate and SpO2 Sensor
- DHT11 Temperature and Humidity Sensor
- Blynk App (for monitoring data)
- Jumper Wires
- Breadboard (optional, for prototyping)

## Software Tools

- MicroPython: The main programming environment for the ESP32.
- Thonny or uPyCraft IDE: Used to write and upload code to the ESP32.
- Blynk App: Used to visualize sensor data and receive alerts.
- Python: The requests library is used to send data to the Blynk API.
- uRequests (MicroPython): A MicroPython version of the `requests` library to send data to Blynk.

## Wiring Diagram

- DHT11 Temperature Sensor:
  - VCC → 3.3V on ESP32
  - GND → GND on ESP32
  - DATA → GPIO 4 on ESP32

- MAX30100 Heart Rate Sensor:
  - VCC → 3.3V on ESP32
  - GND → GND on ESP32
  - SDA → GPIO 21 on ESP32
  - SCL → GPIO 22 on ESP32

## Installation

1. Install MicroPython on your ESP32 board by following the official [MicroPython ESP32 Installation Guide](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).
2. Connect your sensors (DHT11 and MAX30100) to the ESP32 as shown in the wiring diagram.
3. Install Libraries:
   - `machine`, `time`, `dht`, and `I2C` are built-in libraries in MicroPython.
   - Install the `uRequests` library using:
     `''python
     import upip
     upip.install('micropython-urequests')
     ```
4. Create a Blynk Account:
   - Download the Blynk app on your phone.
   - Create a new project and get your Auth Token.
   - Use this token in the provided Python code.

## Code Explanation

### Key Functions:

- `read_sensors()`: Reads data from the DHT11 (temperature) and MAX30100 (heart rate) sensors.
- `send_data_to_blynk(v0, v1)`: Sends the sensor data (temperature and heart rate) to Blynk virtual pins `v0` and `v1`.
- `send_notification(message)`: Sends an alert to the Blynk app if conditions (high heart rate or temperature) are met.
- `check_and_notify(temperature, heart_rate)`: Monitors the readings and sends a notification if either exceeds predefined thresholds (temperature > 37.5°C, heart rate > 120 bpm).

### Running the Code:

1. Upload the code to your ESP32 using the Thonny or uPyCraft IDE.
2. Open the REPL (interactive prompt) to monitor sensor output and ensure the system is reading data.
3. The ESP32 will continuously read the sensors and send data to the Blynk app.

## Troubleshooting

- Ensure your ESP32 is properly connected to your computer or power source.
- Make sure the Blynk Auth Token is correctly set in the code.
- Check your sensor wiring if the readings are incorrect or not updating.

## Contribution

Feel free to contribute to this project by opening an issue or submitting a pull request. Any improvements, suggestions, or bug fixes are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [Blynk](https://blynk.io) for providing an excellent platform to build IoT projects.
- [MicroPython](https://micropython.org) for enabling Python programming on microcontrollers.
- [MAX30100 Heart Rate Sensor](https://www.electronicwings.com/nodemcu/max30100-heart-rate-and-spo2-sensor-interfacing-with-nodemcu) for making heart rate monitoring easy and accessible.