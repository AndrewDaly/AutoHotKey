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


#
# Main loop to detect the chord
while True:
    if keyboard.is_pressed('j') and keyboard.is_pressed('t'):
        j_t()
    if keyboard.is_pressed('j'):
        print('blocking k')
        keyboard.block_key('k')
        if keyboard.is_pressed('k'):
            j_k()
    time.sleep(0.1)  # Short delay for efficient CPU usage
    try:
        keyboard.unblock_key('k')
        print('k unblocked')
    except KeyError:
        pass



#
# #keyboard.add_hotkey('ctrl', toggle_logging)  # Toggle logging on/off
# keyboard.add_hotkey('j', temp_test_function)
#
# #keyboard.hook(log_key)
#
# # Keep the script running to capture all events
# keyboard.wait('esc')  # Press 'esc' to stop logging