#include <stdio.h>
#include <math.h>
#include <windows.h>

double getFrequency(int midiNote);

void playNote(int midiNote, int duration);

double getFrequency(int midiNote) {
    return 440.0 * pow(2.0, (midiNote - 69) / 12.0);
}

void playNote(int midiNote, int duration) {
    double freq = getFrequency(midiNote);
    Beep((unsigned long)freq, duration);
}