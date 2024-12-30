#include <iostream>
#include <windows.h>
#include <cstring>
#include <map>

using namespace std;

map<int, bool> keyState;         // Map to track key states dynamically
bool J_Permissable = false;      // Flag to determine if 'J' should be sent to input

bool isJPressed = false;  // Track if 'J' is pressed
bool isKPressed = false;  // Track if 'K' is pressed
bool isAPressed = false;  // Track if 'A' is pressed
bool isIPressed = false;  // Track if 'I' is pressed
bool isGPressed = false;  // Track if 'G' is pressed
bool isFPressed = false;  // Track if 'F' is pressed

HANDLE pipe;  // Global pipe handle

// Helper function to send a message through the pipe
void sendMessage(const char* message) {
    if (pipe == INVALID_HANDLE_VALUE) {
        cerr << "Pipe handle is invalid!" << endl;
        return;
    }

    string messageWithDelimiter = string(message) + "\n"; // Add a delimiter
    DWORD bytesWritten;

    if (!WriteFile(pipe, messageWithDelimiter.c_str(), messageWithDelimiter.size(), &bytesWritten, NULL)) {
        cerr << "Failed to write to pipe. Error: " << GetLastError() << endl;
    } else {
        cout << "Message sent: " << message << endl;
    }
}

// Functions for specific key combinations
void simjk() { sendMessage("jk"); }
void simja() { sendMessage("ja"); }
void simji() { sendMessage("ji"); }
void simjg() { sendMessage("jg"); }
void simjf() { sendMessage("jf"); }

// Keyboard hook procedure
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT* p = (KBDLLHOOKSTRUCT*)lParam;

        if (wParam == WM_KEYDOWN) {
            switch (p->vkCode) {
                case 0x4A:  // 'J'
                    isJPressed = true;
                    cout << "'J' key pressed!" << endl;
                    if (J_Permissable == false){
                        return 1;
                    }
                    break;
                case 0x4B:  // 'K'
                    isKPressed = true;
                    break;
                case 0x41:  // 'A'
                    isAPressed = true;
                    break;
                case 0x49:  // 'I'
                    isIPressed = true;
                    break;
                case 0x47:  // 'G'
                    isGPressed = true;
                    break;
                case 0x46:  // 'F'
                    isFPressed = true;
                    if (isJPressed) {
                        J_Permissable = true;
                    }
                    break;
            }

            // Handle key combinations
            if (isJPressed && isKPressed) { simjk(); isKPressed = false; return 1; }
            if (isJPressed && isAPressed) { simja(); isAPressed = false; return 1; }
            if (isJPressed && isIPressed) { simji(); isIPressed = false; return 1; }
            if (isJPressed && isGPressed) { simjg(); isGPressed = false; return 1; }
            if (isJPressed && isFPressed) { simjf(); isFPressed = false; return 1; }

        }

        if (wParam == WM_KEYUP) {
            switch (p->vkCode) {
                case 0x4A:  // 'J'
                    isJPressed = false;
                    J_Permissable = false;
                    cout << "'J' key released!" << endl;
                    break;
                case 0x4B:  // 'K'
                    isKPressed = false;
                    break;
                case 0x41:  // 'A'
                    isAPressed = false;
                    break;
                case 0x49:  // 'I'
                    isIPressed = false;
                    break;
                case 0x47:  // 'G'
                    isGPressed = false;
                    break;
                case 0x46: // 'F'f
                    isFPressed = false;
                    J_Permissable = false;
                    break;
            }
        }
    }
    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int main() {
    const char* pipeName = "\\\\.\\pipe\\HotkeyPipe";

    // Create named pipe
    pipe = CreateNamedPipe(
        pipeName,
        PIPE_ACCESS_DUPLEX,
        PIPE_TYPE_MESSAGE | PIPE_READMODE_MESSAGE | PIPE_WAIT,
        1,
        1024,
        1024,
        0,
        NULL
    );

    if (pipe == INVALID_HANDLE_VALUE) {
        cerr << "Failed to create pipe. Error: " << GetLastError() << endl;
        return 1;
    }

    cout << "Waiting for a client to connect..." << endl;

    BOOL connected = ConnectNamedPipe(pipe, NULL) ||
                     (GetLastError() == ERROR_PIPE_CONNECTED);
    if (!connected) {
        cerr << "Failed to connect client. Error: " << GetLastError() << endl;
        CloseHandle(pipe);
        return 1;
    }

    cout << "Client connected!" << endl;

    // Set up the keyboard hook
    HHOOK hook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, NULL, 0);
    if (hook == NULL) {
        cerr << "Failed to install hook!" << endl;
        return 1;
    }

    cout << "Press key combinations with 'J' (e.g., 'J+K', 'J+A', 'J+I', 'J+G')." << endl;
    cout << "Press 'Esc' to exit." << endl;

    // Message loop
    MSG msg;
    while (true) {
        if (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
            if (msg.message == WM_KEYDOWN && msg.wParam == VK_ESCAPE) {
                break;
            }
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    // Cleanup
    UnhookWindowsHookEx(hook);
    CloseHandle(pipe);
    return 0;
}
