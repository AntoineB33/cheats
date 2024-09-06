#Requires AutoHotkey v2.0
#SingleInstance


; Define the log file path (you can change the path)
logFilePath := A_ScriptDir "\keylog.txt"
; Function to log events
LogEvent(event) {
    global logFilePath
    FileAppend(Format("{1}: {2}`n", A_Now, event), logFilePath)  ; Append event to the log file
}

d::{
    LogEvent("event")
    while (GetKeyState("D", "P")) {
        SendEvent("{x down}")
        Sleep(40)
        SendEvent("{x up}")
    }
}
f::c
Space::z

Esc::ExitApp  ; Exit the script when 'Enter' is pressed