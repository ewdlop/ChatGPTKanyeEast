from midiutil import MIDIFile

# Create a MIDI object
midi = MIDIFile(4)  # Four tracks for piano, drums, bass, and guitar

# Tempo and volume settings
tempo = 120
volume = 100

# Tracks
PIANO_TRACK = 0
DRUMS_TRACK = 1
BASS_TRACK = 2
GUITAR_TRACK = 3
LYRICS_TRACK = 4

# Set tempo for all tracks
for track in range(4):
    midi.addTempo(track, 0, tempo)

# ====== Piano Melody ======
piano_notes = [
    (60, 0.5), (67, 0.5), (69, 0.5), (72, 0.5),
    (67, 0.5), (69, 0.5), (72, 0.5), (76, 0.5),
    (72, 0.5), (74, 0.5), (76, 0.5), (79, 0.5),
    (76, 0.5), (74, 0.5), (72, 0.5), (69, 0.5),
]
time = 0
for note, duration in piano_notes:
    midi.addNote(PIANO_TRACK, 0, note, time, duration, volume)
    time += duration

# ====== Drums ======
drum_pattern = [
    (36, 1.0),  # Kick
    (38, 1.0),  # Snare
    (42, 0.5),  # Hi-hat
]
time = 0
for i in range(16):  # 16 beats
    for drum, duration in drum_pattern:
        if drum == 36 and i % 4 == 0:  # Kick on beats 1 and 3
            midi.addNote(DRUMS_TRACK, 9, drum, time, duration, volume)
        elif drum == 38 and i % 4 == 2:  # Snare on beats 2 and 4
            midi.addNote(DRUMS_TRACK, 9, drum, time, duration, volume)
        elif drum == 42:  # Hi-hats on every beat
            midi.addNote(DRUMS_TRACK, 9, drum, time, duration, volume)
        time += duration

# ====== Bass ======
bass_notes = [
    (36, 1.0), (43, 1.0), (45, 1.0), (41, 1.0),  # Root notes: C, G, A, F
]
time = 0
for _ in range(4):  # Repeat for 4 measures
    for note, duration in bass_notes:
        midi.addNote(BASS_TRACK, 1, note, time, duration, volume)
        time += duration

# ====== Guitar ======
guitar_chords = [
    (60, 0.5), (64, 0.5), (67, 0.5), (72, 0.5),  # C Major chord
]
time = 0
for _ in range(16):  # Repeat for 16 beats
    for note, duration in guitar_chords:
        midi.addNote(GUITAR_TRACK, 2, note, time, duration, volume)
        time += duration

# ====== Lyrics ======
# Replace curly quotes and special characters
lyrics = [
    (0, "Oh,"), (1, "you"), (2, "have"), (3, "ChatGPT"),
    (4, "write"), (5, "that?"), (6, "Guess"), (7, "I'll"),
    (8, "own"), (9, "it,"), (10, "yeah,"), (11, "tip"),
    (12, "my"), (13, "hat!"),
]
for time, word in lyrics:
    clean_word = word.encode('ascii', errors='ignore').decode('ascii')  # Ensure ASCII compatibility
    midi.addText(PIANO_TRACK, time, clean_word)

# Save the MIDI file
with open("oh_you_have_chatgpt_with_lyrics_fixed.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI file with lyrics created: oh_you_have_chatgpt_with_lyrics_fixed.mid")
