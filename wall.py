import os
import ctypes
import requests
from PIL import Image

# URL of the image you want to set as wallpaper
image_url = 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg'

# Download the image
response = requests.get(image_url)
image_path = 'wallpaper.jpg'
with open(image_path, 'wb') as file:
    file.write(response.content)

# Set the downloaded image as wallpaper
SPI_SETDESKWALLPAPER = 0x0014
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(image_path), 3)

# Optionally, delete the downloaded image
os.remove(image_path)
