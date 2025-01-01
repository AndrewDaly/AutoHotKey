import os
import time
import pyautogui
import time
import pyautogui
import uiautomation as automation
import pygetwindow
import keyboard
import threading
import tkinter as tk
import itertools


PIPE_NAME = r'\\.\pipe\HotkeyPipe'
print(PIPE_NAME)



current_window = ""

def create_transparent_fullscreen_window(coords):
    # Initialize the main window as the transparent background
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.5)
    root.attributes("-topmost", True)
    root.focus_force()

    # Dictionary to store buttons by their labels
    buttons = {}

    # Generate unique two-character labels
    letters = "abcdefghiklmnopqrstuvwxyz"
    labels = ["".join(pair) for pair in itertools.product(letters, repeat=2)]

    # Iterate over each (x, y) coordinate pair and corresponding label
    for (x, y), label in zip(coords, labels):
        # Create a 10x10 button with a unique two-character label and yellow background
        button = tk.Button(root, text=label, width=2, height=1, bg="yellow")

        # Store the button in the dictionary with the label as the key
        buttons[label] = button

        # Center the button around (x, y) by placing it
        button.place(x=x, y=y-5, width=20, height=20)

    # Create a variable to store typed keys
    typed_keys = ""

    def on_key(event):
        print("on key invoked " + str(event.char))
        nonlocal typed_keys
        # Append the pressed key to the typed keys
        typed_keys += event.char

        # Check if typed_keys matches any button label
        if typed_keys in buttons:
            buttons[typed_keys].invoke()
            print(f"Button ' {typed_keys}' clicked")
            bt = buttons[typed_keys]
            x_coord = bt.winfo_x() + 40
            y_coord = bt.winfo_y() + 20
            print(x_coord)
            print(y_coord)
            root.destroy()
            pyautogui.moveTo(x_coord, y_coord)
            pyautogui.doubleClick(x_coord, y_coord)
            # Reset typed keys after a match
            typed_keys = ""

        elif len(typed_keys) >= 2:
            # Reset typed keys
            typed_keys = ""
    # Bind key pressed to the button layer
    root.bind("<Key>", on_key)

    # Event binding for exiting fullscreen with ESC key
    root.bind("<Escape>", lambda e: root.destroy())
    root.focus_force()
    root.mainloop()

coordinate_list = []

def list_all_children(control, level=0):
    # Indent the output to visualize the hierarchy
    indent = "  " * level

    # Get the bounding rectangle (x, y) coordinates
    rect = control.BoundingRectangle
    if rect:
        x, y = rect.left, rect.top
        #print(f"Coordinates: ({x}, {y})")
        coordinates = (x, y)
    else:
        coordinates = "Coordinates not available"

    print(f"Control Name: {control.Name}, Control Type: {control.ControlTypeName}, {coordinates}")
    if control.ControlTypeName != 'EditControl':
        coordinate_list.append(coordinates)

    children = control.GetChildren()
    for child in children:
        list_all_children(child, level + 1)

def automation_task_non_threaded():
    desktop = automation.GetRootControl()
    active_window = pygetwindow.getActiveWindowTitle()
    for window in desktop.GetChildren():

        if window.Name == active_window:
            print(f"Top-level window: {window.Name}")
            list_all_children(window)
            create_transparent_fullscreen_window(coordinate_list)


def listen_for_hotkeys():
    while True:
        try:
            # Open the pipe (this will block until the server connects)
            with open(PIPE_NAME, 'r') as pipe:
                for message in pipe:
                    print(f"Received message: {message.strip()}")
                    #message = pipe.read()

                    print(f"Received: {message}")
                    if 'ja' in message:
                        print('ja')
                        pyautogui.hotkey('ctrl', 'a')
                    if 'jc' in message:
                        print('jc')
                        pyautogui.hotkey('ctrl', 'c')
                    if 'jf' in message:
                        print('jf')
                        pyautogui.press('j')
                    if 'jg' in message:
                        print('jg')
                        pyautogui.hotkey('alt', 'tab')
                    if 'ji' in message:
                        print('ji')
                        pyautogui.press('up')
                    if 'jk' in message:
                        print('jk')
                        pyautogui.press('down')
                    if 'jl' in message:
                        print('jl')
                        pyautogui.hotkey('ctrl', 'l')
                    if 'jo' in message:
                        print('jo')
                        pyautogui.hotkey('ctrl','pgup')
                    if 'jp' in message:
                        print('jp')
                        pyautogui.hotkey('ctrl','pgdn')
                    if 'jr' in message:
                        print('jr')
                        pyautogui.hotkey('ctrl', 'r')
                    if 'js' in message:
                        print('js')
                        pyautogui.hotkey('ctrl', 's')
                    if 'jt' in message:
                        print('jt')
                        pyautogui.hotkey('ctrl', 't')
                    if 'jv' in message:
                        print('jv')
                        pyautogui.hotkey('ctrl', 'v')
                    if 'jw' in message:
                        print('jw')
                        pyautogui.hotkey('ctrl', 'w')
                    if 'jq' in message:
                        print('jq')
                        automation_task_non_threaded()


        except IOError:
            # Wait for the pipe to be available
            print("Waiting for pipe...")
            time.sleep(1)

if __name__ == "__main__":
    listen_for_hotkeys()



