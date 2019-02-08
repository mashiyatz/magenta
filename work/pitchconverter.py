import numpy as np

class PitchConverter:

    def __init__(self):
        return

    def convert(self, note_values):
        if not isinstance(note_values, (list,)):
            note_values = list(note_values)
        else:
            pass
        if isinstance(note_values[0], (str,)):
            midi_pitch = self.name_to_pitch(note_values)
        elif isinstance(note_values[0], (float, int)):
            midi_pitch = self.freq_to_pitch(note_values)
        else:
            midi_pitch = 0
        return midi_pitch

    @staticmethod
    def name_to_pitch(notes):
        name_to_pitch_dict = {}
        return name_to_pitch_dict

    @staticmethod
    def freq_to_pitch(freqs):
        pitch = freqs*10
        return pitch
