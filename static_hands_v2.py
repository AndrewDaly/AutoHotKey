import keyboard
import time
import string

# Define a threshold in seconds for detecting near-simultaneous key presses
TIME_THRESHOLD = 0.2  # 200 milliseconds
OTHER_KEY_THRESHOLD = 0.2
# Track the last time 'j' was pressed and a dictionary to track each other letter's press time
last_j_press = 0
last_not_j_press = 0
last_other_press = {letter: 0 for letter in string.ascii_lowercase if letter != 'j'}

def print_chord(letter):
    print(f"j + {letter} chord detected")
    if letter == 'a':
        keyboard.send('ctrl+a')
    if letter == 'b':
        pass
    if letter == 'c':
        keyboard.send('ctrl+c')
    if letter == 'd':
        keyboard.send('left')
    if letter == 'e':
        keyboard.send('ctrl+e')
    if letter == 'f':
        keyboard.send('right')
    if letter == 'g':
        keyboard.send('ALT+TAB')
    if letter == 'i':
        keyboard.send('up')
    if letter == 'k':
        keyboard.send('down')
    if letter == 'l':
        keyboard.send('ctrl+l')
    if letter == 'o':
        keyboard.send(keyboard.KEY_UP)
    if letter == 'p':
        keyboard.send(keyboard.KEY_DOWN)
    if letter == 'n':
        keyboard.send('ctrl+n')
    if letter == 'r':
        keyboard.send('ctrl+r')
    if letter == 's':
        keyboard.send('ctrl+s')
    if letter == 't':
        keyboard.send('ctrl+t')
    # ~j & v:: Send("{CTRL Down}{v}{CTRL Up}")
    # ~j & w:: Send("{CTRL Down}{w}{CTRL Up}")
    # ~j & x:: Send("{CTRL Down}{x}{CTRL Up}")
    # ~j & z:: Send("{CTRL Down}{z}{CTRL Up}")
    # ~j & SPACE::Send("{BACKSPACE}")

# Function to handle 'j' key press
def on_j_press(event):
    global last_j_press
    last_j_press = time.time()  # Update 'j' press timestamp

    # Block all other alphabet keys while 'j' is pressed
    for letter in last_other_press.keys():
        keyboard.block_key(letter)
    print("All other keys are blocked while 'j' is pressed")
    #time.sleep(0.1)

# Function to handle 'j' key release
def on_j_release(event):
    # Unblock all other alphabet keys when 'j' is released
    for letter in last_other_press.keys():
        keyboard.unblock_key(letter)
    print("All other keys are unblocked")
    #time.sleep(0.1)

# Function to handle other alphabet key presses
def on_other_press(event):
    print('on_other_press ' + str(event.name))
    global last_other_press, last_j_press
    letter = event.name  # Get the letter pressed

    current_letter_press = time.time()
    global last_not_j_press

    if letter in last_other_press:
        last_other_press[letter] = time.time()  # Update the timestamp for the letter

        # Check if 'j' was pressed recently within the threshold
        if last_other_press[letter] - last_j_press < TIME_THRESHOLD:
            print_chord(letter)  # Call function for j + letter chord
            return False

        # TODO: addin some error handling for the TypeError that sometimes occurs
        if current_letter_press - lacst_not_j_press < OTHER_KEY_THRESHOLD:
            keyboard.send(letter)
    last_not_j_press = time.time()
    return True  # Suppress the letter from being sent to input

# Hook 'j' key with its press and release handlers
keyboard.hook_key('j', on_j_press, suppress=True)
keyboard.on_release_key('j', on_j_release)

# Hook all other letters a-z except 'j'
for letter in last_other_press.keys():
    keyboard.hook_key(letter, on_other_press, suppress=True)

# Keep the program running
keyboard.wait('esc')  # Program ends when 'Esc' is pressed
