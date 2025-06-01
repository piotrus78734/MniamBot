from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

# Inicjalizacja I2C, domyślny adres 0x3C
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

with canvas(device) as draw:
    draw.text((10, 10), "Hello OLED!", fill=255)