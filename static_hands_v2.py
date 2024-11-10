import keyboard
import time

# Define a threshold in seconds for detecting near-simultaneous key presseskk
TIME_THRESHOLD = 0.1  # 200 milliseconds

# Track the last time 'j' and 'k' were pressed
last_j_press = time.time()
last_k_press = time.time()

def j_k_chord():
    print("jk chord detected")

# Function to handle 'j' key press
def on_j_press(event):
    global last_j_press, last_k_press
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in letters:
        keyboard.block_key(i)

    print('last j press: ' + str(last_j_press))
    # Check if 'k' was pressed recently within the threshold
    print('time between presses ' + str(last_k_press - last_j_press))
    if last_k_press - last_j_press < TIME_THRESHOLD:
        if last_k_press - last_j_press > 0:
            j_k_chord()
            last_k_press = 0
            last_j_press = 0
    try:
        for i in letters:
            keyboard.unblock_key(i)
    except KeyError:
        pass
    last_j_press = time.time()  # Update 'j' press timestamp
    return False


# Function to handle 'k' key presskkk
def on_k_press(event):
    global last_k_press
    last_k_press = time.time()  # Update 'k' press timestamp
    print('last k press: ' + str(last_k_press))
    if last_k_press - last_j_press > TIME_THRESHOLD:
        return True
    else:
        return False
    # try:
    #     keyboard.unblock_key('k')
    # except KeyError:
    #     pass
    # return False

# Hook 'j' and 'k' keys with their respective handlers and suppress them
keyboard.on_press_key('j', on_j_press, suppress=True)
keyboard.on_press_key('k', on_k_press, suppress=True)
#keyboard.on_release_key('j', on_j_release)
#keyboard.add_hotkey('j+k', j_k_chord(), suppress=True, timeout=3)

# Keep the program running
keyboard.wait('esc')  # Program ends when 'Esc' is pressed
