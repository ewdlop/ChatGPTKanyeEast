##!/usr/bin/python3

#!pip install midiutil
#!pip3 install midiutil

from midiutil import MIDIFile

# Create a MIDI object
midi = MIDIFile(1)  # One track
track = 0
time = 0  # Start at the beginning
channel = 0
volume = 100  # Volume

# Set up the tempo and key signature
tempo = 120
midi.addTempo(track, time, tempo)

# Define the melody
notes = [
    (60, 1), (67, 1), (69, 1), (72, 1),  # "Oh, you have ChatGPT write that"
    (67, 1), (69, 1), (72, 1), (76, 1),  # "Guess I’ll own it, yeah, tip my hat"
    (72, 1), (74, 1), (76, 1), (79, 1),  # "From the beats to the rhymes, it’s a wild duet"
    (76, 1), (74, 1), (72, 1), (69, 1),  # "Man and machine, we ain’t done yet"
]

# Add notes to the MIDI track
for note, duration in notes:
    midi.addNote(track, channel, note, time, duration, volume)
    time += duration

# Save the MIDI file
with open("oh_you_have_chatgpt_write_that.mid", "wb") as output_file:
    midi.writeFile(output_file)
print("MIDI file created: oh_you_have_chatgpt_write_that.mid")
