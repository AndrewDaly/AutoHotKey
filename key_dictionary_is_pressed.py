import keyboard
import time

THRESHOLD = 0.9

# for each letter assign a boolean for is_pressed
keys = {}
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in letters:
    keys.update({i: False})

# for each letter track the last time it got pressed
last_pressed = {}
for i in last_pressed:
    last_pressed.update({i: 0})

def j_a():
    print('ja chord')
    keyboard.press_and_release('ctrl+a')

def j_t():
    print("Chord 'j' + 't' detected!")  # Replace with your desired action
    keyboard.press_and_release('ctrl+t')

def j_k():
    print('jk chord')
    keyboard.press_and_release('down')

def j_i():
    print('ji chord')
    keyboard.press_and_release('up')

def j_d():
    print('jd chord')
    keyboard.press_and_release('left')

def j_f():
    print('jf chord')
    keyboard.press_and_release('right')



def update_keys(e):
    letter = e.name
    print('letter pressed: ' + str(letter))
    current_time = time.time()
    last_pressed.update({letter: current_time})
    print(last_pressed.get(letter))

    if letter == 'j':
        print('j press detected')
        return False

    last_j_press = last_pressed.get('j')
    # check we are within the threshold
    try:
        if current_time - last_j_press < THRESHOLD:
            print('we are within threshold')
            if letter == 'a':
                j_a()
            if letter == 'i':
                j_i()
                return False
            if letter == 'k':
                j_k()
                return False
    except TypeError: #check against type errors when j has not been pressed yet
        pass
    return True
def on_j_press(e):
    print('ooook')
    last_pressed.update({'j': time.time()})

keyboard.on_press(update_keys, suppress=True)
keyboard.on_press_key('j',on_j_press, suppress=True)
keyboard.wait('esc')