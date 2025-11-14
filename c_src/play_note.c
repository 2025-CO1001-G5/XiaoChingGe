#include <stdio.h>
#include <math.h>
#include <windows.h>

double getFrequency(int midiNote);

void playNote(int midiNote, int duration);

//int main() {
//
//    int notes[] = {
//        48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,  // C3 ~ B3
//        60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,  // C4 ~ B4
//        72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,  // C5 ~ B5
//    };
//    int length = sizeof(notes) / sizeof(notes[0]);
//
//    for (int i = 0; i < length; i++) {
//        playNote(notes[i], 1000);
//        Sleep(50);
//    }                                                    //上面是我用來測試的
//    return 0;
//}
double getFrequency(int midiNote) {
    return 440.0 * pow(2.0, (midiNote - 69) / 12.0);
}

void playNote(int midiNote, int duration) {
    double freq = getFrequency(midiNote);
    Beep((unsigned long)freq, duration);
}