from PIL import Image, ImageDraw
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)
device.contrast(255)
device.clear()

image = Image.new("1", device.size)
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Hello OLED!", fill=255)

device.display(image)