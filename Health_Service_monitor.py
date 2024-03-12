# Import necessary libraries for Pico and LCD
from machine import I2C, Pin, ADC
from ssd1306 import SSD1306_I2C
import utime
import os

# Initialize I2C for the LCD
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = SSD1306_I2C(128, 64, i2c)

# Initialize ADC for battery voltage measurement
adc = ADC(Pin(26))  # Assuming you have connected the battery voltage to GPIO 26

# Function to get CPU temperature in Celsius
def get_cpu_temperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            temperature = int(file.read()) / 1000.0
            return temperature
    except Exception as e:
        print("Error reading CPU temperature:", e)
        return None

# Function to get battery voltage
def get_battery_voltage():
    try:
        # Assuming you have a voltage divider (e.g., 2:1) connected to GPIO 26
        voltage = adc.read_u16() / 65535 * 3.3 * 2
        return voltage
    except Exception as e:
        print("Error reading battery voltage:", e)
        return None

# Function to display text on the LCD
def display_text(text):
    lcd.fill(0)
    lcd.text(text, 0, 0)
    lcd.show()

# Main loop
while True:
    try:
        # Get CPU temperature
        cpu_temperature = get_cpu_temperature()

        # Get battery voltage
        battery_voltage = get_battery_voltage()

        if cpu_temperature is not None and battery_voltage is not None:
            # Display CPU temperature and battery voltage on the LCD
            display_text(f'CPU Temp: {cpu_temperature:.2f} C\nBattery Voltage: {battery_voltage:.2f} V')

            # Add additional monitoring and actions here based on your requirements

        # Sleep for a few seconds before the next iteration
        utime.sleep(5)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C) to exit gracefully
        print("Exiting monitoring loop.")
        break
    except Exception as e:
        print("Error:", e)
