import time
from pynput.keyboard import Key, Controller, Listener
from datetime import datetime

# Initialize the keyboard controller
keyboard = Controller()

# Define the log file path
log_file_path = "keylog.txt"

# List to hold active keys
keys = []

# Function to log events to a file
def log_event(event):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now()}: {event}\n")

# Function to simulate key presses/releases
def press_on(key):
    keyboard.press(key)
    time.sleep(0.03)  # Simulate a brief press
    keyboard.release(key)

# Function to handle key interrupt and simulate transitions between key states
def interrupt(start):
    global keys
    if len(keys) != 1:
        for i, item in enumerate(keys[-1]):
            new_key = keys[-1][i]
            if item != new_key:
                if not start:
                    intermediary = new_key
                    new_key = item
                    item = intermediary
                keyboard.release(item)  # Simulate key up
                if new_key != "Up":
                    keyboard.press(new_key)  # Simulate key down
    else:
        for new_key in keys[-1]:
            action = keyboard.release if not start else keyboard.press
            if new_key != "Up":
                action(new_key)

# Function to simulate holding a key while another key is pressed
def hit(key, key_to_press):
    while True:
        if not is_key_pressed(key):
            break
        press_on(key_to_press)

# Function to check if a key is pressed
def is_key_pressed(key):
    # This will work for standard letters, extend for special keys if needed
    with Listener(on_press=None, on_release=None) as listener:
        return key in listener.canonical(key)

# Function to activate key combinations
def activate(key, keys_to_push, key_to_press="x"):
    global keys
    keys.append(keys_to_push)
    interrupt(True)
    hit(key, key_to_press)
    interrupt(False)
    keys.pop()

# Function to handle key press and release
def on_press(key):
    try:
        if key.char == 't':
            activate('t', [Key.left, Key.up])
        elif key.char == 'g':
            activate('g', [Key.left, Key.down])
        elif key.char == 'i':
            activate('i', [Key.right, Key.up])
        elif key.char == 'j':
            activate('j', [Key.right, Key.down])
        elif key.char == 'r':
            activate('r', [Key.left, Key.up], 'a')
        elif key.char == 'o':
            activate('o', [Key.right, Key.up], 'a')
        elif key.char == ' ':
            press_on('z')
        elif key.char == 'p':
            press_on('c')
        elif key.char == 'h':
            press_on(Key.up)
    except AttributeError:
        pass

# Function to exit the program on pressing the 'Esc' key
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Start listening for key press/release events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    