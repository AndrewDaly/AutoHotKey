import ctypes
from ctypes import wintypes
import atexit

# Define the foo function
def foo():
    print("Function foo executed!")

# Constants
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
VK_J = 0x4A  # Virtual-Key code for "J"

# Define ULONG_PTR manually
ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)

# Structures for low-level keyboard hooks
class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", wintypes.DWORD),
        ("scanCode", wintypes.DWORD),
        ("flags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]

# Low-level keyboard hook callback
def low_level_keyboard_proc(nCode, wParam, lParam):
    if nCode == 0 and wParam == WM_KEYDOWN:  # Check if key is pressed
        key_struct = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        if key_struct.vkCode == VK_J:  # Check if the key is "J"
            foo()  # Call your custom function
    return ctypes.windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)

# Set up the hook
HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
hook_proc = HOOKPROC(low_level_keyboard_proc)

# Install the hook
hook_id = ctypes.windll.user32.SetWindowsHookExW(WH_KEYBOARD_LL, hook_proc, ctypes.windll.kernel32.GetModuleHandleW(None), 0)

if not hook_id:
    raise RuntimeError("Failed to install keyboard hook")

# Ensure the hook is removed when the program exits
@atexit.register
def unregister_hook():
    if hook_id:
        ctypes.windll.user32.UnhookWindowsHookEx(hook_id)

# Run a message loop to keep the hook active
try:
    msg = wintypes.MSG()
    while ctypes.windll.user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))
except KeyboardInterrupt:
    print("Exiting...")
