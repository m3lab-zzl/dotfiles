#Requires AutoHotkey v2
^!r:: Reload ; ctrl + alt + r; reload the script
; launch some app with hotkey

^!l::
{
    if WinExist("ahk_exe Logseq.exe") {
        WinActivate
    }
    else {
        MsgBox("Logseq...", , "T1")
        home := EnvGet("USERPROFILE")
        Run home "\AppData\Local\Logseq\Logseq.exe"
    }
}

^!o::
{
    if WinExist("ahk_exe ONENOTE.exe") {
        WinActivate
    }
    else {
        MsgBox("Onenote...", , "T1")
        home := EnvGet("USERPROFILE")
        Run "ONENOTE.EXE"
    }
}


^!f::
{
    if WinExist("ahk_exe Firefox.exe") {
        WinActivate
    }
    else {
        MsgBox("Firefox...", , "T1")
        home := EnvGet("USERPROFILE")
        Run "C:\Program Files\Mozilla Firefox\firefox.exe"
    }
}

^!w::
{
    if WinExist("ahk_exe wezterm.exe") {
        WinActivate
    }
    else {
        MsgBox("wezterm...", , "T1")
        home := EnvGet("USERPROFILE")
        Run "C:\Program Files\Wezterm\wezterm.exe"
    }
}


~LShift & WheelUp:: ; Scroll left.
{
    If WinActive("ahk_exe WINWORD.EXE")
    {
        fcontrol := ControlGetClassNN(ControlGetFocus("A Loop 1")) ; <-- Increase or decrease this value to scroll faster or slower.
        ComObjActive("Word.application").ActiveWindow.SmallScroll(0, 0, 0, 1)
        return
    }
    else if WinActive("ahk_exe POWERPNT.EXE")
    {
        fcontrol := ControlGetClassNN(ControlGetFocus("A Loop 1")) ; <-- Increase or decrease this value to scroll faster or slower.
        ComObjActive("PowerPoint.application").ActiveWindow.SmallScroll(0, 0, 0, 1)
        return
    }
    else if WinActive("ahk_exe EXCEL.EXE")
    {
        fcontrol := ControlGetClassNN(ControlGetFocus("A Loop 1")) ; <-- Increase or decrease this value to scroll faster or slower.
        ComObjActive("Excel.application").ActiveWindow.SmallScroll(0, 0, 0, 1)
        return
    }
    else
        {
            SendInput("{WheelLeft}")
            return
        }
}
~LShift & WheelDown:: ; Scroll right.
{
    If WinActive("ahk_exe WINWORD.EXE")
    {
        fcontrol := ControlGetClassNN(ControlGetFocus("A Loop 1")) ; <-- Increase or decrease this value to scroll faster or slower.
        ComObjActive("Word.application").ActiveWindow.SmallScroll(0, 0, 1, 0)
        return
    }
    else if WinActive("ahk_exe POWERPNT.EXE")
    {
        fcontrol := ControlGetClassNN(ControlGetFocus("A Loop 1")) ; <-- Increase or decrease this value to scroll faster or slower.
        ComObjActive("PowerPoint.application").ActiveWindow.SmallScroll(0, 0, 1, 0)
        return
    }
    else if WinActive("ahk_exe EXCEL.EXE")
    {
        fcontrol := ControlGetClassNN(ControlGetFocus("A Loop 1")) ; <-- Increase or decrease this value to scroll faster or slower.
        ComObjActive("Excel.application").ActiveWindow.SmallScroll(0, 0, 1, 0)
        return
    }
    else
    {
        SendInput("{WheelRight}")
        return
    }
}
; ------ Based on https://gist.github.com/erbanku/eac274bc41baf6fd100013020a8de151, and converted to v2 ------
;Switch between Light & Dark Mode on Windows 11
;IN THIS CASE, APPS ON WINDOWS 11 WILL USE LIGHT/DARK MODE
^!T:: ; ctrl alt t
; read current theme
{ ; V1toV2: Added bracket
    MsgBox("toggle dark theme", , "T1")
    Apptheme := RegRead("HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme")
    ; toggle between themes
    RegWrite(1 - Apptheme, "REG_DWORD", "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme")
    Systheme := RegRead("HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme")
    ; toggle between themes
    RegWrite(1 - Systheme, "REG_DWORD", "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme")
    Return
    ;IN THIS CASE, SYSTEMS ON WINDOWS 11 WILL USE LIGHT/DARK MODE
} ; V1toV2: Added Bracket before hotkey or Hotstring
; Ctrl-Alt-Z: stick on top
^!z::
{
    WinSetAlwaysOnTop -1, "A"
}
