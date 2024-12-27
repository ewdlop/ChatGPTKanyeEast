import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI()

# Create an instrument (a piano in this case)
instrument = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano

# Define the melody (notes and their durations)
notes = [
    (60, 0.5), (67, 0.5), (69, 0.5), (72, 0.5),  # "Oh, you have ChatGPT write that"
    (67, 0.5), (69, 0.5), (72, 0.5), (76, 0.5),  # "Guess I’ll own it, yeah, tip my hat"
    (72, 0.5), (74, 0.5), (76, 0.5), (79, 0.5),  # "From the beats to the rhymes, it’s a wild duet"
    (76, 0.5), (74, 0.5), (72, 0.5), (69, 0.5),  # "Man and machine, we ain’t done yet"
]

# Time to start each note
start_time = 0.0

# Add the notes to the instrument
for pitch, duration in notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + duration)
    instrument.notes.append(note)
    start_time += duration

# Add the instrument to the PrettyMIDI object
midi.instruments.append(instrument)

# Write the MIDI data to a file
midi.write("oh_you_have_chatgpt_write_that.mid")
print("MIDI file created: oh_you_have_chatgpt_write_that.mid")
