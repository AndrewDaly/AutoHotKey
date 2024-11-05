import keyboard
import time

THRESHOLD = 0.3

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

def j_b():
    print('jb chord')
    keyboard.press_and_release('ctrl+b')
def j_c():
    print('jc chord')
    keyboard.press_and_release('ctrl+c')
def j_d():
    print('jd chord')
    keyboard.press_and_release('left')
def j_e():
    print('je chord')
    keyboard.press_and_release('ctrl+e')
def j_f():
    print('jf chord')
    keyboard.press_and_release('ctrl+f')
def j_g():
    print('jg chord')
    keyboard.press_and_release('alt+tab')
def j_h():
    print('jh chord')
    keyboard.press_and_release('j')#
def j_i():
    print('ji chord')
    keyboard.press_and_release('up')
def j_l():
    print('jl chord')
    keyboard.press_and_release('ctrl+l')
def j_m():
    print('jm chord')
    keyboard.press_and_release('ctrl+m')
def j_n():
    print('jn chord')
    keyboard.press_and_release('ctrl+n')
def j_o():
    print('jo chord')
    keyboard.press_and_release('ctrl+page up')
def j_p():
    print('jp chord')
    keyboard.press_and_release('ctrl+page down')
def j_r():
    print('jr chord')
    keyboard.press_and_release('ctrl+r')
def j_t():
    print("Chord 'j' + 't' detected!")  # Replace with your desired action
    keyboard.press_and_release('ctrl+t')

def j_s():
    print('js')
    keyboard.press_and_release('ctrl+s')
def j_w():
    print('jw')
    keyboard.press_and_release('ctrl+w')
def j_z():
    print('jz')
    keyboard.press_and_release('ctrl+z')
def j_k():
    print('jk chord')
    keyboard.press_and_release('down')
#
# def j_i():
#     print('ji chord')
#     keyboard.press_and_release('up')
#
# def j_d():
#     print('jd chord')
#     keyboard.press_and_release('left')
#
# def j_f():
#     print('jf chord')
#     keyboard.press_and_release('right')



def update_keys(e):
    letter = e.name
    #print('letter pressed: ' + str(letter))
    current_time = time.time()
    last_pressed.update({letter: current_time})
    #print(last_pressed.get(letter))

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
                return False
            if letter == 'b':
                j_b()
                return False
            if letter == 'c':
                j_c()
                return False
            if letter == 'd':
                j_d()
                return False
            if letter == 'e':
                j_e()
                return False
            if letter == 'f':
                j_f()
                return False
            if letter == 'g':
                j_g()
            if letter == 'h':
                j_h()
                return False
            if letter == 'i':
                j_i()
                return False
            if letter == 'k':
                j_k()
                return False
            if letter == 'l':
                j_l()
                return False
            if letter == 'm':
                j_m()
                return False
            if letter == 'n':
                j_n()
                return False
            if letter == 'o':
                j_o()
                return False
            if letter == 'p':
                j_p()
                return False
            if letter == 'r':
                j_r()
                return False
            if letter == 's':
                j_s()
                return False
            if letter == 't':
                j_t()
                return False
            if letter == 'w':
                j_w()
            if letter == 'z':
                j_z()
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