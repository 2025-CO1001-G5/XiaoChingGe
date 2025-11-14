from ctypes import *
from importlib.resources import files
from ctypes import cdll

LIB_NAME = "play_note.so"

def load_my_library():
    lib_path = files('src.app.backend').joinpath('libs', LIB_NAME).resolve()
    return cdll.LoadLibrary(lib_path)

def play_note(midi_note: int, duration: int):
    module = load_my_library()
    module.playNote(c_int(midi_note), c_long(duration))