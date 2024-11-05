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

def update_keys(e):
    print('letter pressed: ' + str(e.name))
    current_time = time.time()
    last_pressed.update({e.name: current_time})
    print(last_pressed.get(e.name))

    if e.name == 'j':
        print('j press detected')
        return False

    last_j_press = last_pressed.get('j')
    # check we are within the threshold
    try:
        if current_time - last_j_press < THRESHOLD:
            print('we are within threshold')
    except TypeError: #check against type errors when j has not been pressed yetj
        pass
def on_j_press(e):
    print('ooook')
    last_pressed.update({'j': time.time()})

keyboard.on_press(update_keys)
keyboard.on_press_key('j',on_j_press, suppress=True)
keyboard.wait('esc')