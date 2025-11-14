from ctypes import *
module = cdll.LoadLibrary("./_lib/play_sound.so")

def play_sound(midi_note: int, duration: int):
    module.play_sound(c_int(midi_not), c_long(duration))