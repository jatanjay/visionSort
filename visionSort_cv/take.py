import sys
import time
from picamera2 import Picamera2, Preview


picam2 = Picamera2()

def capture_image(file_name):

    file_path = f'/home/jp/Desktop/visionSort/visionSort_cv/{file_name}.jpg'
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (320, 240)}, display="lores")
    picam2.configure(camera_config)
    picam2.start()
    picam2.capture_file(file_path)

    print(f"Image captured and saved to {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_name>")
    else:
        file_name = sys.argv[1]
        capture_image(file_name)