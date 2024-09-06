import pyautogui
import time
import keyboard
from datetime import datetime

# Log file path
log_file_path = 'keylog.txt'

# Function to log events
def log_event(event):
    with open(log_file_path, 'a') as f:
        f.write(f"{datetime.now()}: {event}\n")

# Function to simulate "x" keypress
def hold_x_while_d_pressed():
    log_event("D key pressed")
    while keyboard.is_pressed('d'):
        pyautogui.keyDown('x')
        time.sleep(0.04)  # Sleep for 40 ms
        pyautogui.keyUp('x')

# Mapping 'f' to 'c'
def remap_f_to_c():
    log_event("F key remapped to C")
    pyautogui.press('c')

# Mapping 'space' to 'z'
def remap_space_to_z():
    log_event("Spacebar remapped to Z")
    pyautogui.press('z')

# Exit function when Esc is pressed
def exit_script():
    log_event("Script exited")
    exit()

# Keyboard event listeners
keyboard.add_hotkey('d', hold_x_while_d_pressed)
keyboard.add_hotkey('f', remap_f_to_c)
keyboard.add_hotkey('space', remap_space_to_z)
keyboard.add_hotkey('esc', exit_script)

# Keep the script running
log_event("Script started")
keyboard.wait('esc')
