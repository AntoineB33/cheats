#Requires AutoHotkey v2.0
#SingleInstance

; Define the log file path (you can change the path)
logFilePath := A_ScriptDir "\keylog.txt"

keys := []

; Function to log events
LogEvent(event) {
    global logFilePath
    FileAppend(Format("{1}: {2}`n", A_Now, event), logFilePath)  ; Append event to the log file
}

interrupt(start) {
    if(keys.Length != 1) {
        for index, item in keys[keys.Length - 1] {
            newKey := keys[keys.Length][index]
            if (item != newKey) {
                if (!start) {
                    intermediary := newKey
                    newKey := item
                    item := intermediary
                }
                SendEvent("{" item " up}")
                if(newKey != "Up") {
                    SendEvent("{" newKey " down}")
                }
            }
        }
    } else {
        for index, newKey in keys[keys.Length] {
            mvt := "up"
            if(start) {
                mvt := "down"
            }
            if(newKey != "Up") {
                SendEvent("{" newKey " " mvt "}")
            }
        }
    }
}

pressOn(key) {
    SendEvent("{" key " down}")
    Sleep(25)
    SendEvent("{" key " up}")
}

hit(key, keyToPress) {
    ; Suspend False
    while (GetKeyState(key, "P")) {
        pressOn(keyToPress)
    }
    ; Suspend True
}

activate(key, keyToPush, keyToPress := "x") {
    ; Suspend True
    global keys
    keys.Push(keyToPush)
    interrupt(true)
    hit(key, keyToPress)
    interrupt(false)
    keys.Pop()
    ; Suspend False
}

t:: activate("T", ["Left", "Up"])
g:: activate("G", ["Left", "Down"])
i:: activate("I", ["Right", "Up"])
j:: activate("J", ["Right", "Down"])
r:: activate("R", ["Left", "Up"], "A")
o:: activate("O", ["Right", "Up"], "A")

Space:: pressOn("z")
p:: pressOn("c")
h:: pressOn("Up")

Esc::ExitApp  ; Exit the script when 'Enter' is pressed