import keyboard  # Import the library
from datetime import datetime
import time

keyboard.block_key('j')

# toggle the global variable logging enabled
logging_enabled = True
def toggle_logging():
    global logging_enabled
    logging_enabled = not logging_enabled
    print(f"Logging {'enabled' if logging_enabled else 'disabled'}")

j_pressed = True
def j_toggle():
    print("toggling j")
    global j_pressed
    j_pressed = not j_pressed

# function that logs keystrokes
def log_key(e):
    if logging_enabled:
        with open("key_data.log", "a") as log_file:
            log_file.write(f"{datetime.now()} - {e.name}\n")  # Log timestamp and key

def temp_test_function():
    print('hotkey summoned control flow to here')

def j_t():
    print("Chord 'j' + 't' detected!")  # Replace with your desired action
    keyboard.press_and_release('ctrl+t')

def j_k():
    print('jk chord')
    keyboard.press_and_release('down')

def j_i():
    print('ji chord')
    keyboard.press_and_release('up')

def j_d():
    print('jd chord')
    keyboard.press_and_release('left')

def j_f():
    print('jf chord')
    keyboard.press_and_release('right')



#
# Main loop to detect the chord

while True:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if keyboard.is_pressed('j'):
        for i in letters:
            keyboard.block_key(i)
    # if keyboard.is_pressed('j') and keyboard.is_pressed('t'):
    #     j_t()
    if keyboard.is_pressed('j'):
        keyboard.block_key('k')
        if keyboard.is_pressed('k'):
            j_k()
        keyboard.unblock_key('k')
    if keyboard.is_pressed('j'):
        keyboard.block_key('i')
        if keyboard.is_pressed('i'):
            j_i()
        keyboard.block_key('i')
    if keyboard.is_pressed('j'):
        keyboard.block_key('d')
        if keyboard.is_pressed('d'):
            j_d()
        keyboard.unblock_key('d')
    if keyboard.is_pressed('j'):
        keyboard.block_key('f')
        if keyboard.is_pressed('f'):
            j_f()
        keyboard.unblock_key('f')
    #time.sleep(0.1)
    try:
        for i in letters:
            keyboard.unblock_key(i)
        #print('k unblocked')
    except KeyError:
        pass
    time.sleep(0.1)

#
# #keyboard.add_hotkey('ctrl', toggle_logging)  # Toggle logging on/off
# keyboard.add_hotkey('j', temp_test_function)
#
# #keyboard.hook(log_key)
#
# # Keep the script running to capture all events
# keyboard.wait('esc')  # Press 'esc' to stop logging