import os
import time
import pyautogui

PIPE_NAME = r'\\.\pipe\HotkeyPipe'
print(PIPE_NAME)
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
                        pyautogui.press('ctrl','pgup')
                    if 'jp' in message:
                        print('jp')
                        pyautogui.hotkey('ctrl','pgdwn')
                    if 'jr' in message:
                        print('jr')
                        pyautogui.hotkey('ctrl', 'r')
                    if 'js' in message:
                        print('js')
                        pyautogui.hotkey('ctrl', 's')
                    if 'jt' in message:
                        print('jt')
                        pyautogui.hotkey('ctrl', 't')
                    if 'jw' in message:
                        print('jw')
                        pyautogui.hotkey('ctrl', 'w')

        except IOError:
            # Wait for the pipe to be available
            print("Waiting for pipe...")
            time.sleep(1)

if __name__ == "__main__":
    listen_for_hotkeys()
