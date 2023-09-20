#Author: Dhayaneshwar
#Github: github.com/dhayanesh
import pystray
import ctypes
from PIL import Image, ImageDraw
from pystray import MenuItem as item
import keyboard

def is_capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) != 0  # VK_CAPITAL is 0x14

def create_image(caps_on):
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    dc = ImageDraw.Draw(image)
    if caps_on:
        margin_width = width * 0.1
        margin_height = height * 0.1
        dc.ellipse((margin_width, margin_height, width - margin_width, height - margin_height), fill="white")
    return image


def set_icon(icon=None):
    if is_capslock_on():
        icon.icon = create_image(True)
    else:
        icon.icon = create_image(False)
    icon.visible = True

def on_activate(icon, item):
    icon.stop()

icon = pystray.Icon("CapsLock Status")
icon.menu = pystray.Menu(item('Exit', on_activate))
keyboard.hook(lambda e: set_icon(icon) if e.name == 'caps lock' else None)
icon.run(lambda icon: set_icon(icon))
