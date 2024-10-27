#Requires AutoHotkey v2.0

#SingleInstance

CapsLock & Esc::ExitApp()

#UseHook
SendMode "Input"
SetWorkingDir A_ScriptDir

~j & a:: Send("{CTRL Down}{a}{CTRL Up}")
~j & b:: Send("{Shift Down}{Tab}{Shift Up}")
~j & C:: Send("{CTRL Down}{c}{CTRL Up}")
;~j & d:: Send("{ALT Down}{SHIFT Down}{ESC}{SHIFT UP}{ALT Up}") 
~j & d:: Send("{Blind}{Left}")
~j & e:: Send("{CTRL Down}{e}{CTRL Up}") 
;~j & f:: Send("{ALT Down}{ESC}{ALT Up}") 
~j & f:: Send("{Blind}{Right}")
~j & h:: Send("{Tab}") 
~j & g:: Send("{ALT Down}{SHIFT Down}{ESC}{SHIFT UP}{ALT Up}") 
~j & i:: Send("{Blind}{Up}") 
~j & k:: Send("{Blind}{Down}") 
~j & l:: Send("{CTRL DOwn}{l}{CTRL Up}") 
~j & o:: Send("{CTRL Down}{Pgup}{CTRL Up}")
~j & n:: Send("{CTRL Down}{n}{CTRL Up}")
~j & p:: Send("{CTRL Down}{PgDn}{CTRL Up}")
~j & q:: Send("{Lwin}")
~j & r:: Send("{CTRL Down}{r}{CTRL Up}")
~j & S:: Send("{CTRL Down}{S}{CTRL up}")
~j & t:: Send("{CTRL Down}{t}{CTRL Up}")
~j & v:: Send("{CTRL Down}{v}{CTRL Up}")
~j & w:: Send("{CTRL Down}{w}{CTRL Up}")
~j & x:: Send("{CTRL Down}{x}{CTRL Up}")
~j & z:: Send("{CTRL Down}{z}{CTRL Up}")
~j & SPACE::Send("{BACKSPACE}")

~j & 1:: Send("{CTRL Down}{1}{CTRL Up}")
~j & 2:: Send("{CTRL Down}{2}{CTRL Up}")
~j & /:: Send("j")
~j & ':: Send("j")

;~j & ':: Send("{Blind}{Right}")
;~j & `;:: Send("{Blind}{Left}")
;

;make d and f left and right 
;make g switch pane

;~j & z:: Send("j")

global jHeld := false

j::
{
	jHeld := true
}