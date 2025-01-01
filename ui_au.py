import time
import pyautogui
import uiautomation as automation
import pygetwindow
import keyboard
import threading
import tkinter as tk
import itertools

current_window = ""

def create_transparent_fullscreen_window(coords):
    # Initialize the main window as the transparent background
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.5)
    root.attributes("-topmost", True)
    root.focus_force()
    # Create a toplevel window for fully opaque buttons
    # button_layer = tk.Toplevel(root)
    # button_layer.attributes("-fullscreen", True)
    # button_layer.attributes("-alpha", 0.4)
    # button_layer.attributes("-topmost", True)
    # button_layer.title("controller_layer")
    #button_layer.focus_force()

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
    #button_layer.bind("<Escape>", lambda e: root.destroy())
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

    #if control.ControlTypeName == 'TabItemControl':
    #if control.ControlTypeName == 'TabControl':
    #print(control.ControlTypeName)
    #if control.ControlTypeName == 'MenuItemControl':
    #if control.ControlTypeName == 'TextControl':
    #if control.ControlTypeName == 'EditControl':
    #if control.ControlTypeName:
    #    print(control.ControlTypeName)

    # ListItemControl

    #if control.ControlTypeName == 'ListItemControl':# or control.ControlTypeName == 'MenuItemControl':
    print(f"Control Name: {control.Name}, Control Type: {control.ControlTypeName}, {coordinates}")
    coordinate_list.append(coordinates)

    children = control.GetChildren()
    for child in children:
        list_all_children(child, level + 1)

def super_cool(event):
    def automation_task():
        initializer = automation.UIAutomationInitializerInThread

        window = automation.WindowControl(searchDepth=1, Name="Downloads")
        if window.Exists(0, 0):
            window.SetActive()
        else:
            print("Window with the title downloads not found")

        desktop = automation.GetRootControl()

        for window in desktop:
            print(f"Top-level window: {window.Name}")

            if window.ClassName == r'CabinetWClass' and pyautogui.getActiveWindowTitle() == window.Name:
                print("List all children of File Explorer with coordinates")
                current_window = pyautogui.getActiveWindowTitle()
                list_all_children(window)
                create_transparent_fullscreen_window(coordinate_list)

        del initializer
    automation_thread = threading.Thread(target=automation_task)
    automation_thread.start()
    automation_thread.join()

def automation_task_non_threaded():
    # window = automation.WindowControl(searchDepth=1, Name="Downloads - File Explorer")
    # if window.Exists(0, 0):
    #     window.SetActive()
    # else:
    #     print("Window with the title downloads not found")

    desktop = automation.GetRootControl()
    for window in desktop.GetChildren():
        print(f"Top-level window: {window.Name}")

        # if window.ClassName == r'CabinetWClass' and pyautogui.getActiveWindowTitle() == window.Name:
        #     print("List all children of File Explorer with coordinates")
        #     current_window = pyautogui.getActiveWindowTitle()
        #     list_all_children(window)
        #     create_transparent_fullscreen_window(coordinate_list)
        if window.Name == 'Downloads - File Explorer':
            print("List all children of File Explorer with coordinates")
            #current_window = pyautogui.getActiveWindowTitle()
            list_all_children(window)
            create_transparent_fullscreen_window(coordinate_list)

if __name__ == '__main__':
    # keyboard.hook_key('Alt', super_cool, suppress=True)
    # keyboard.wait('esc')
    automation_task_non_threaded()
