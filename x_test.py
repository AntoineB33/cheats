import pyautogui
import time

# Number of times to press the 'x' key
number_of_presses = 100  # Adjust this number as needed

# Time interval between each press in seconds
delay_between_presses = 0.1  # Adjust this delay as needed

print("Starting to spam 'x'...")

# Loop to press 'x' the specified number of times
for _ in range(number_of_presses):
    pyautogui.press('x')
    time.sleep(delay_between_presses)

print("Spamming complete.")