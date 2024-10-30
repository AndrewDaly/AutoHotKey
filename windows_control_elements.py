import uiautomation as automation
import time
import tkinter as tk

def list_all_children(control, level=0):
    # Indent the output to visualize the hierarchy
    indent = "  " + str(level)

    # Get the bounding rectangle (x, y coordinates)
    rect = control.BoundingRectangle
    if rect:
        x, y = rect.left, rect.top # Extract the top-left corner coordinates
        coordinates = f"Coordinates:({x}. {y})"
    else:
        coordinates = "Coordinates: Not available"

    # Print control details along with the coordinates (#ListItemControl)
    if control.ControlTypeName == 'ListItemControl':
        print(f"{indent}Control Name: {control.Name}, Control Type: {control.ControlTypeName}, {coordinates})")
        user_input_text = input()
        if user_input_text == 'y':
            time.sleep(5)
            control.Click()


    # Recursively get and list all children of the current control
    children = control.GetChildren()
    for child in children:
        # Recursively call the function for each child
        list_all_children(child, level + 1)

# Get the desktop root control
desktop = automation.GetRootControl()

for window in desktop.GetChildren():


    # If the window is 'File Explorer', list all its children recursively
    if window.Name == 'hotkey - File Explorer':
        print(f"Top-level window: {window.Name}")
        print("list all children of File Explorer with coordinates:")
        list_all_children(window) # Call the recursive function for File Explorer
    # if window.Name == 'other':
        # list_all_children(window)
