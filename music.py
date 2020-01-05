import pandas as pd
import numpy

# define notes and scale intervals
notes = pd.Series(["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"])

major_scale_int = pd.Series([0, 2, 4, 5, 7, 9, 11])
minor_scale_int = pd.Series([0, 2, 3, 5, 7, 8, 10])

# grab input info
maj_min = input("\n \n Is your key major or minor? (M or m) \n \n")
key_letter = input("\n \n Which note is your key? \n \n (Options: C, C#, D, Eb, E, F, F#, G, Ab, A, Bb, B) \n \n")

# find starting root note index number
root = (notes.values == key_letter).argmax()

# function to find key scale
def scale(maj_min, root):

    scale = []

    if maj_min == "M":
        for interval in major_scale_int:
            scale.append(notes[root + interval])
    
    if maj_min == "m":
        for interval in minor_scale_int:
            scale.append(notes[root + interval])
    
    return scale

# display scale
print("\n \n" + str(key_letter) + str(maj_min) + " " + "Scale: " + str(scale(maj_min, root)) + "\n \n")

# save current scale as series
scale = pd.Series(scale(maj_min, root))

# ordered list of notes from key (needed to create chord notes that extend beyond the length of the 'scale' variable)
notes_in = notes[notes.isin(scale)].reset_index(drop=True)

three_note_chords = []
four_note_chords = []

def chords(scale):

    for note in scale:
        three_note_chords.append([note, notes_in[(notes_in.values == note).argmax() + 2], notes_in[(notes_in.values == note).argmax() + 4]])
        four_note_chords.append([note, notes_in[(notes_in.values == note).argmax() + 2], notes_in[(notes_in.values == note).argmax() + 4], notes_in[(notes_in.values == note).argmax() + 6]])
        
    return three_note_chords, four_note_chords

# call chords() on current scale
chords(scale)

# creating chord names for display
if maj_min == "M":
    
    df_index = [(str(scale[0] + " Major")),
            (str(scale[0] + " Major 7th")),
            (str(scale[1] + " Minor")),
            (str(scale[1] + " Minor 7th")),
            (str(scale[2] + " Minor")),
            (str(scale[2] + " Minor 7th")),
            (str(scale[3] + " Major")),
            (str(scale[3] + " Major 7th")),
            (str(scale[4] + " Major")),
            (str(scale[4] + " Dominant 7th")),
            (str(scale[5] + " Minor")),
            (str(scale[5] + " Minor 7th")),
            (str(scale[6] + " Diminished")),
            (str(scale[6] + " Half Diminished"))]

if maj_min == "m":
    
    df_index = [(str(scale[0] + " Minor")),
            (str(scale[0] + " Minor 7th")),
            (str(scale[1] + " Diminished")),
            (str(scale[1] + " Minor 7th flat5")),
            (str(scale[2] + " Major")),
            (str(scale[2] + " Major 7th")),
            (str(scale[3] + " Minor")),
            (str(scale[3] + " Minor 7th")),
            (str(scale[4] + " Minor")),
            (str(scale[4] + " Minor 7th")),
            (str(scale[5] + " Major")),
            (str(scale[5] + " Major 7th")),
            (str(scale[6] + " Major")),
            (str(scale[6] + " Dominant 7th"))]

# collect individual chords to assign to names
data = [[three_note_chords[0]],
        [four_note_chords[0]],
        [three_note_chords[1]],
        [four_note_chords[1]],
        [three_note_chords[2]],
        [four_note_chords[2]],
        [three_note_chords[3]],
        [four_note_chords[3]],
        [three_note_chords[4]],
        [four_note_chords[4]],
        [three_note_chords[5]],
        [four_note_chords[5]],
        [three_note_chords[6]],
        [four_note_chords[6]]]

# create dataframe of chord names and incldued notes
chords_df = pd.DataFrame(index = df_index, data = data, columns = ["Notes"])

print(str(chords_df) + "\n \n")