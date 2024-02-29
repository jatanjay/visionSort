import serial
import time

ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

try:
    while True:
        ser.write(b"Hello from RPI")

        # Read data from ESP32
        received_data = ser.readline().decode("utf-8").strip()
        print(f"Received from ESP32: {received_data}")
        time.sleep(1)

except KeyboardInterrupt:
    ser.close()

