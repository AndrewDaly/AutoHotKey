import keyboard
import time

# Define a threshold in seconds for detecting near-simultaneous key presses
TIME_THRESHOLD = 0.2  # 200 milliseconds

# Track the last time 'j' and 'k' were pressed
last_j_press = 0
last_k_press = 0


def j_k_chord():
    print("jk chord detected")


# Function to handle 'j' key press
def on_j_press(event):
    global last_j_press, last_k_press
    last_j_press = time.time()  # Update 'j' press timestamp

    # Block 'k' key while 'j' is pressed
    keyboard.block_key('k')
    print("'k' is blocked")

    # Check if 'k' was pressed recently within the threshold
    if last_j_press - last_k_press < TIME_THRESHOLD:
        j_k_chord()
    else:
        keyboard.unblock_key('k')
        print('k unblocked')
    return False  # Suppress 'j' from being sent to input


# Function to handle 'j' key release
def on_j_release(event):
    # Unblock 'k' when 'j' is released
    keyboard.unblock_key('k')
    print("'k' is unblocked")


# Function to handle 'k' key press
def on_k_press(event):
    global last_k_press, last_j_press
    last_k_press = time.time()  # Update 'k' press timestamp

    # Check if 'j' was pressed recently within the threshold
    if last_k_press - last_j_press < TIME_THRESHOLD:
        j_k_chord()
        return False   # Suppress 'k' from being sent to inputkkkk

    return True


# Hook 'j' and 'k' keys with their respective handlers and suppress them
keyboard.hook_key('j', on_j_press, suppress=True)
keyboard.hook_key('k', on_k_press, suppress=True)
keyboard.on_release_key('j', on_j_release)

# Keep the program running
keyboard.wait('esc')  # Program ends when 'Esc' is pressed
