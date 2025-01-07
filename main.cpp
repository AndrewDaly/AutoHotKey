#include <iostream>
#include <windows.h>
#include <cstring>
#include <map>

using namespace std;

map<int, bool> keyState;         // Map to track key states dynamically
bool J_Permissable = false;      // Flag to determine if 'J' should be sent to input

bool isAPressed = false;  // Track if 'a' is pressed
bool isCPressed = false;  // Track if 'c' is pressed
bool isFPressed = false;  // Track if 'f' is pressed
bool isGPressed = false;  // Track if 'g' is pressed
bool isIPressed = false;  // Track if 'i' is pressed
bool isJPressed = false;  // Track if 'j' is pressed
bool isKPressed = false;  // Track if 'k' is pressed
bool isLPressed = false;  // Track if 'l' is pressed
bool isOPressed = false;  // Track if 'o' is pressed
bool isPPressed = false;  // Track if 'p' is pressed
bool isQPressed = false;  // Track if 'q' is pressed
bool isRPressed = false;  // Track if 'r' is pressed
bool isSPressed = false;  // Track if 's' is pressed
bool isTPressed = false;  // Track if 't' is pressed
bool isVPressed = false;  // Track if 'v' is pressed
bool isWPressed = false;  // Track if 'w' is pressed


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
void simja() { sendMessage("ja"); }
void simjc() { sendMessage("jc"); }
void simjf() { sendMessage("jf"); }
void simjg() { sendMessage("jg"); }
void simji() { sendMessage("ji"); }
void simjk() { sendMessage("jk"); }
void simjl() { sendMessage("jl"); }
void simjo() { sendMessage("jo"); }
void simjp() { sendMessage("jp"); }
void simjr() { sendMessage("jr"); }
void simjs() { sendMessage("js"); }
void simjt() { sendMessage("jt"); }
void simjv() { sendMessage("jv"); }
void simjw() { sendMessage("jw"); }
void simjq() { sendMessage("jq"); }


// Keyboard hook procedure
LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT* p = (KBDLLHOOKSTRUCT*)lParam;

        if (wParam == WM_KEYDOWN) {
            switch (p->vkCode) {
                case 0x41:  // 'A'
                    isAPressed = true;
                break;

                case 0x43:  // 'C'
                    isCPressed = true;
                break;

                case 0x46:  // 'F'
                    isFPressed = true;
                if (isJPressed) {
                    J_Permissable = true;
                }
                break;

                case 0x47:  // 'G'
                    isGPressed = true;
                break;

                case 0x49:  // 'I'
                    isIPressed = true;
                break;

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

                case 0x4c:  // 'L'
                    isLPressed = true;
                break;

                case 0x4f:  // 'O'
                    isOPressed = true;
                break;

                case 0x50:  // 'P'
                    isPPressed = true;
                break;

                case 0x51: // 'Q'
                    isQPressed = true;
                break;

                case 0x52: // 'R'
                    isRPressed = true;
                break;

                case 0x53: // 'S'
                    isSPressed = true;
                break;

                case 0x54:  // 'T'
                    isTPressed = true;
                break;

                case 0x57:  // 'W'
                    isWPressed = true;
                break;

                case 0x56:  // 'V'
                    isVPressed = true;
                break;
            }

            // Handle key combinations
            if (isJPressed && isAPressed) { simja(); isAPressed = false; return 1; }
            if (isJPressed && isCPressed) { simjc(); isCPressed = false; return 1; }
            if (isJPressed && isFPressed) { simjf(); isFPressed = false; return 1; }
            if (isJPressed && isGPressed) { simjg(); isGPressed = false; return 1; }
            if (isJPressed && isIPressed) { simji(); isIPressed = false; return 1; }
            if (isJPressed && isKPressed) { simjk(); isKPressed = false; return 1; }
            if (isJPressed && isLPressed) { simjl(); isLPressed = false; return 1; }
            if (isJPressed && isOPressed) { simjo(); isOPressed = false; return 1; }
            if (isJPressed && isPPressed) { simjp(); isPPressed = false; return 1; }
            if (isJPressed && isRPressed) { simjr(); isRPressed = false; return 1; }
            if (isJPressed && isSPressed) { simjs(); isSPressed = false; return 1; }
            if (isJPressed && isTPressed) { simjt(); isTPressed = false; return 1; }
            if (isJPressed && isVPressed) { simjv(); isVPressed = false; return 1; }
            if (isJPressed && isWPressed) { simjw(); isWPressed = false; return 1; }
            if (isJPressed && isQPressed) { simjq(); isQPressed = false; return 1; }
        }

        if (wParam == WM_KEYUP) {
            switch (p->vkCode) {
                case 0x4A:  // 'J'
                    isJPressed = false;
                    J_Permissable = false;
                    cout << "'J' key released!" << endl;
                    break;

                case 0x46: // 'F'f
                    isFPressed = false;
                    J_Permissable = false;
                    break;

                case 0x41:  // 'A'
                    isAPressed = false;
                break;

                case 0x43:  // 'C'
                    isCPressed = false;
                break;

                case 0x47:  // 'G'
                    isGPressed = false;
                break;

                case 0x49:  // 'I'
                    isIPressed = false;
                break;

                case 0x4B:  // 'K'
                    isKPressed = false;
                break;

                case 0x4c:  // 'L'
                    isLPressed = false;
                break;

                case 0x4f:  // 'O'
                    isOPressed = false;
                break;

                case 0x50:  // 'P'
                    isPPressed = false;
                break;

                case 0x51: // 'Q'
                    isQPressed = false;
                break;

                case 0x52: // 'R'
                    isRPressed = false;
                break;

                case 0x53: // 'S'
                    isSPressed = false;
                break;

                case 0x54:  // 'T'
                    isTPressed = false;
                break;

                case 0x57:  // 'W'
                    isWPressed = false;
                break;

                case 0x56:  // 'V'
                    isVPressed = false;
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
