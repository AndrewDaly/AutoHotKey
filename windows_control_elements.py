import uiautomation as automation
import tkinter as tk
import time


def list_all_children(control, level=0):
    """
    Recursively lists all child controls of a given control and displays a label on the canvas
    for each ListItemControl with its name at its coordinates.
    """
    rect = control.BoundingRectangle
    if rect:
        x, y = rect.left, rect.top  # Top-left corner coordinates

        # Display label if it is a ListItemControl
        if control.ControlTypeName == 'ListItemControl':
            label_text = f"{control.ControlTypeName}: ({x}, {y})"
            print(label_text)  # For debugging purposes

            # Check for user input to proceed with clicking
            user_input_text = input("Press 'y' to click on this control or any other key to continue: ")

            if user_input_text.lower() == 'y':
                control.Click()
                print("Clicked on control.")

                root = tk.Tk()



    # Recursively process child controls
    for child in control.GetChildren():
        list_all_children(child, level + 1)



# Main code execution
desktop = automation.GetRootControl()
for window in desktop.GetChildren():
    if window.Name == 'hotkey - File Explorer':
        print(f"Top-level window: {window.Name}")
        print("Listing all children of File Explorer with coordinates:")

        # Start listing children of the targeted window and labeling them on canvas
        list_all_children(window)
