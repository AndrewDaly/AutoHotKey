#Requires AutoHotkey v2.0

#SingleInstance

CapsLock & Esc::ExitApp()

#UseHook
SendMode "Input"
SetWorkingDir A_ScriptDir

~j & a:: Send("{CTRL Down}{a}{CTRL Up}")
~j & b:: Send("{Shift Down}{Tab}{Shift Up}")
~j & C:: Send("{CTRL Down}{c}{CTRL Up}") 
~j & d:: Send("{ALT Down}{SHIFT Down}{ESC}{SHIFT UP}{ALT Up}") 
~j & e:: Send("{CTRL Down}{e}{CTRL Up}") 
~j & f:: Send("{ALT Down}{ESC}{ALT Up}") 
~j & g:: Send("{Tab}") 
~j & h:: Send("{Alt Down){Left}{Alt Up}") 
~j & i:: Send("{Blind}{Up}") 
~j & k:: Send("{Blind}{Down}") 
~j & l:: Send("{CTRL DOwn}{l}{CTRL Up}") 
~j & o:: Send("{CTRL Down}{Pgup}{CTRL Up}") 
~j & p:: Send("{CTRL Down}{PgDn}{CTRL Up}")
~j & q:: Send("{Lwin}")
~j & r:: Send("{CTRL Down}{r}{CTRL Up}")
~j & S:: Send("{CTRL Down}{S}{CTRL up}")
~j & t:: Send("{CTRL Down}{t}{CTRL Up}")
~j & v:: Send("{CTRL Down}{V}{CTRL Up}")
~j & w:: Send("{CTRL Down}{w}{CTRL Up}")
~j & 1:: Send("{CTRL DOwn}{1}{CTRL Up}")
~j & 2:: Send("{CTRL DOwn}{2}(CTRL Up}")

~j & z:: Send("j")

global jHeld := false

j::
{
	jHeld := true
}