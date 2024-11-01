import keyboard
import time
import string

# Define a threshold in seconds for detecting near-simultaneous key presses
TIME_THRESHOLD = 0.2  # 200 milliseconds

# Track the last time 'j' was pressed and a dictionary to track each other letter's press time
last_j_press = 0
last_other_press = {letter: 0 for letter in string.ascii_lowercase if letter != 'j'}

def print_chord(letter):
    print(f"j + {letter} chord detected")

# Function to handle 'j' key press
def on_j_press(event):
    global last_j_press
    last_j_press = time.time()  # Update 'j' press timestamp

    # Block all other alphabet keys while 'j' is pressed
    for letter in last_other_press.keys():
        keyboard.block_key(letter)
    print("All other keys are blocked while 'j' is pressed")

# Function to handle 'j' key release
def on_j_release(event):
    # Unblock all other alphabet keys when 'j' is released
    for letter in last_other_press.keys():
        keyboard.unblock_key(letter)
    print("All other keys are unblocked")

# Function to handle other alphabet key presses
def on_other_press(event):
    print('on_other_press')
    global last_other_press, last_j_press
    letter = event.name  # Get the letter pressed

    if letter in last_other_press:
        last_other_press[letter] = time.time()  # Update the timestamp for the letter

        # Check if 'j' was pressed recently within the threshold
        if last_other_press[letter] - last_j_press < TIME_THRESHOLD:
            print_chord(letter)  # Call function for j + letter chord
            return False

    return True  # Suppress the letter from being sent to input

# Hook 'j' key with its press and release handlers
keyboard.hook_key('j', on_j_press, suppress=True)
keyboard.on_release_key('j', on_j_release)

# Hook all other letters a-z except 'j'
for letter in last_other_press.keys():
    keyboard.hook_key(letter, on_other_press, suppress=True)

# Keep the program running
keyboard.wait('esc')  # Program ends when 'Esc' is pressed
