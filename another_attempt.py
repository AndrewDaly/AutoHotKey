from pyhooked import Hook, KeyboardEvent
import keyboard
# Function to handle key events
def handle_event(event):
    global j_pressed

    # Check if the event is a keyboard event
    if isinstance(event, KeyboardEvent):
        if event.current_key == 'J' and event.event_type == 'key down':
            j_pressed = True
            print("J key pressed")

        if event.current_key == 'K' and event.event_type == 'key down' and j_pressed:
            print("J + K chord detected!")
            j_pressed = False  # Reset

        if event.current_key == 'J' and event.event_type == 'key up':
            j_pressed = False
            print("J key released")

# Initialize the global state
j_pressed = False
keyboard.block_key('j')
# Create the hook object
hk = Hook()
hk.handler = handle_event  # Set the handler
print("Listening for key events... (Press Ctrl+C to exit)")

try:
    hk.hook()  # Start the hook
except KeyboardInterrupt:
    print("\nExiting...")

print('done')