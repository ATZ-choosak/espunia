from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
from PIL import ImageFont, ImageDraw, Image
import time
import datetime
 
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=2)

def FirstDis():
    text = "Preset : Grand Piano"
    width = device.width
    height = device.height
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    fontsize = 15
    font = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Bold.ttf", fontsize)  # Replace with your font path and size
    max_text_width = 128 

    display_width = device.width
    display_height = device.height

    lines = []
    line = ""
    for word in text.split():
        if font.getbbox(line + word)[2] <= display_width:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    x = 0
    y = 0

    for line in lines:
        draw.text((x, y), line, font=font, fill=255)
        y += font.getbbox(line)[3] 

    device.display(image)

def PREDIS(t):

    device.clear()
    text = t
    width = device.width
    height = device.height
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    fontsize = 15
    font = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Bold.ttf", fontsize)  # Replace with your font path and size
    max_text_width = 128 

    display_width = device.width
    display_height = device.height

    lines = []
    line = ""
    for word in text.split():
        if font.getbbox(line + word)[2] <= display_width:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    x = 0
    y = 0

    for line in lines:
        draw.text((x, y), line, font=font, fill=255)
        y += font.getbbox(line)[3] 

    device.display(image)

def OCDIS(t):

    device.clear()
    text = t
    width = device.width
    height = device.height
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    fontsize = 15
    font = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Bold.ttf", fontsize)  # Replace with your font path and size
    max_text_width = 128 

    display_width = device.width
    display_height = device.height

    lines = []
    line = ""
    for word in text.split():
        if font.getbbox(line + word)[2] <= display_width:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    x = 0
    y = 0

    for line in lines:
        draw.text((x, y), line, font=font, fill=255)
        y += font.getbbox(line)[3] 

    device.display(image)
