import keyboard
import time
import string

def print_chord(letter):
    print(f"j + {letter} chord detected")
    if letter == 'a':
        keyboard.send('ctrl+a')
    if letter == 'b':
        pass
    if letter == 'c':
        keyboard.send('ctrl+c')
    if letter == 'd':
        keyboard.send('left')
    if letter == 'e':
        keyboard.send('ctrl+e')
    if letter == 'f':
        keyboard.send('right')
    if letter == 'g':
        keyboard.send('ALT+TAB')
    if letter == 'i':
        keyboard.send('up')
    if letter == 'k':
        keyboard.send('down')
    if letter == 'l':
        keyboard.send('ctrl+l')
    if letter == 'o':
        keyboard.send(keyboard.KEY_UP)
    if letter == 'p':
        keyboard.send(keyboard.KEY_DOWN)
    if letter == 'n':
        keyboard.send('ctrl+n')
    if letter == 'r':
        keyboard.send('ctrl+r')
    if letter == 's':
        keyboard.send('ctrl+s')
    if letter == 't':
        keyboard.send('ctrl+t')
    # ~j & v:: Send("{CTRL Down}{v}{CTRL Up}")
    # ~j & w:: Send("{CTRL Down}{w}{CTRL Up}")
    # ~j & x:: Send("{CTRL Down}{x}{CTRL Up}")
    # ~j & z:: Send("{CTRL Down}{z}{CTRL Up}")
    # ~j & SPACE::Send("{BACKSPACE}")

def handler():
    print('handler called')
    if keyboard.is_pressed('k'):
        keyboard.send('down')


#keyboard.block_key('j')
keyboard.on_press_key('j', handler, suppress=True)

# in this configuration, j doesn't get hooked
# keyboard.block_key('j')
# keyboard.hook_key('j', handler)

# Keep the program running
keyboard.wait('esc')  # Program ends when 'Esc' is pressed
