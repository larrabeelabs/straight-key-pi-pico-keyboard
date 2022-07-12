# Circuit Python 
# keyboard for Pi Pico to be used with hamradio.solutions/vband/

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keypress_pin = board.GP21  # connect one side of your key to GP21, other side to GND
# Our array of key objects
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.LEFT_CONTROL] #[Keycode.RIGHT_BRACKET, Keycode.LEFT_BRACKET]
control_key = False #Keycode.SHIFT

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

switch = digitalio.DigitalInOut(board.GP21)
switch.switch_to_input(pull=digitalio.Pull.UP)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Waiting for key pin...")

while True:
    if not switch.value:
        print("Pin is grounded.")

        led.value = True
        key = keys_pressed[0]  # Get the corresponding Keycode or string
        keyboard.press(control_key, key)  # "Press"...
        time.sleep(0.03)
        led.value = False

    else:

        keyboard.release_all()  # ..."Release"!
        
