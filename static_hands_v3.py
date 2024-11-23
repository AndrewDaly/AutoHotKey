import keyboard
import pyautogui
import time

def send_ctrl(key):
    """Helper function to send CTRL + key."""
    pyautogui.hotkey('ctrl', key)

def handle_chords(key):
    """Handles all 'j' + key combinations."""
    if key == 'a':
        send_ctrl('a')
    elif key == 'b':
        pyautogui.hotkey('shift', 'tab')
    elif key == 'c':
        send_ctrl('c')
    elif key == 'd':
        pyautogui.press('left')
    elif key == 'e':
        send_ctrl('e')
    elif key == 'f':
        pyautogui.press('right')
    elif key == 'g':
        pyautogui.hotkey('alt', 'shift', 'esc')
    elif key == 'h':
        pyautogui.press('tab')
    elif key == 'i':
        pyautogui.press('up')
    elif key == 'k':
        pyautogui.press('down')
    elif key == 'l':
        send_ctrl('l')
    elif key == 'o':
        send_ctrl('pgup')
    elif key == 'n':
        send_ctrl('n')
    elif key == 'p':
        send_ctrl('pgdn')
    elif key == 'q':
        pyautogui.press('win')
    elif key == 'r':
        send_ctrl('r')
    elif key == 's':
        send_ctrl('s')
    elif key == 't':
        send_ctrl('t')
    elif key == 'v':
        send_ctrl('v')
    elif key == 'w':
        send_ctrl('w')
    elif key == 'x':
        send_ctrl('x')
    elif key == 'z':
        send_ctrl('z')
    elif key == 'space':
        pyautogui.press('backspace')
    elif key == '1':
        send_ctrl('1')
    elif key == '2':
        send_ctrl('2')
    elif key == '/':
        pyautogui.typewrite('j')
    elif key == "'":
        pyautogui.typewrite('j')

# Event handler for key presses with 'j' held down
def on_key_down(event):
    if event.name == 'j':
        # Block the 'j' key
        keyboard.block_key('j')

        # Wait for another key to be pressed for the chord
        chord_key = keyboard.read_event(suppress=True).name
        handle_chords(chord_key)  # Handle the chord combination
    else:
        # Allow normal input for other keys if 'j' is not held
        keyboard.unblock_key(event.name)

# Hook the keyboard listener
keyboard.on_press(on_key_down)

# Keep the script running
keyboard.wait('esc')  # Press 'esc' to stop the script