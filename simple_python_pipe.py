import os
import time

PIPE_NAME = r'\\.\pipe\HotkeyPipe1'
print(PIPE_NAME)
def listen_for_hotkeys():
    while True:
        try:
            # Open the pipe (this will block until the server connects)
            with open(PIPE_NAME, 'r') as pipe:
                message = pipe.read()
                print(f"Received: {message}")
                if message == "J pressed":
                    print("Action for J pressed")
                elif message == "K pressed":
                    print("Action for K pressed")
        except IOError:
            # Wait for the pipe to be available
            print("Waiting for pipe...")
            time.sleep(1)

if __name__ == "__main__":
    listen_for_hotkeys()
