import time
import pyautogui
import uiautomation as automation
import pygetwindow
import keyboard
import threading
import tkinter as tk
import itertools

current_window = ""

def create_ui(coords):
    # Initialize the main window as the transparent background
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.5)
    root.attributes("-topmost", True)
    root.focus_force()
    buttons = {}
    letters = "abcdefghiklmnopqrstuvwxyz"
    labels = ["".join(pair) for pair in itertools.product(letters, repeat=2)]

    for (x, y), label in zip(coords, labels):
        button = tk.Button(root, text=label, width=2, height=1, bg="yellow")
        buttons[label] = button
        button.place(x=x, y=y-5, width=20, height=20)

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
            #pyautogui._mouseMoveDrag(x_coord, y_coord)
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
    #root.focus_force()
    root.mainloop()

coordinate_list = []
def list_all_children(control, level=0):
    indent = "  " * level
    rect = control.BoundingRectangle
    if rect:
        x, y = rect.left, rect.top
        print(f"Coordinates: ({x}, {y})")
        coordinates = (x, y)
    else:
        coordinates = "Coordinates not available"
    if control.ControlTypeName == 'ListItemControl' or control.ControlTypeName == 'MenuItemControl':
        print(f"{indent}Control Name: {control.Name}, Control Type: {control.ControlTypeName}, {coordinates}")
        coordinate_list.append(coordinates)
    children = control.GetChildren()
    for child in children:
        list_all_children(child, level + 1)

def automation_task_non_threaded():
    print("non threaded execution started")
    desktop = automation.GetRootControl()
    for window in desktop.GetChildren():
        # print(f"Top-level window: {window.Name}")
        if window.Name == 'Downloads - File Explorer':
            print("List all children of File Explorer with coordinates")
            list_all_children(window)
            # This creates the coordinate list
            create_ui(coordinate_list)
    # with automation.InitializeUIAutomationInCurrentThread():
    #     desktop = automation.GetRootControl()
    #     for window in desktop.GetChildren():
    #         # print(f"Top-level window: {window.Name}")
    #         if window.Name == 'Downloads - File Explorer':
    #             print("List all children of File Explorer with coordinates")
    #             list_all_children(window)
    #             # This creates the coordinate list
    #             create_ui(coordinate_list)

if __name__ == '__main__':
    print("*************************")
    #keyboard.add_hotkey('alt', automation_task_non_threaded)
    automation_task_non_threaded()
    #keyboard.wait('esc')  # Press 'esc' to stop logging
