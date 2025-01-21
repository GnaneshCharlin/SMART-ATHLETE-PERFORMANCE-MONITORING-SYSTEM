import time
import requests
from machine import Pin, I2C
import dht
from max30100 import MAX30100

BLYNK_AUTH_TOKEN = 'YourAuthToken'
BLYNK_URL = f'https://blynk.cloud/external/api/update?token={BLYNK_AUTH_TOKEN}'

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
max30100 = MAX30100(i2c)

dht_pin = Pin(4, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT11(dht_pin)

def send_data_to_blynk(v0, v1):
    params = {
        'v0': v0,
        'v1': v1
    }
    response = requests.get(BLYNK_URL, params=params)
    return response

def send_notification(message):
    notification_url = f'https://blynk.cloud/external/api/notify?token={BLYNK_AUTH_TOKEN}&text={message}'
    response = requests.get(notification_url)
    return response

def check_and_notify(temperature, heart_rate):
    if heart_rate > 120:
        send_notification('Warning: High Heart Rate Detected!')
    if temperature > 37.5:
        send_notification('Warning: High Body Temperature Detected!')

def read_sensors():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        heart_rate = max30100.read_heart_rate()

        if heart_rate is None:
            heart_rate = 'Failed to read'

        print(f"Temperature: {temperature} °C")
        print(f"Heart Rate: {heart_rate} bpm")

        send_data_to_blynk(temperature, heart_rate)
        check_and_notify(temperature, heart_rate)

    except Exception as e:
        print(f"Error: {e}")

while True:
    read_sensors()
    time.sleep(2)
