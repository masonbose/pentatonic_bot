major_pent = [{"C": "C, D, E, G, A, C"},
              {"C#": "C#, D#, F, G#, A#, C#"},
              {"Db": "Db, Eb, F, Ab, Bb, Db"},
              {"D": "D, E, F#, A, B, D"},
              {"Eb": "Eb, F, G, Bb, C, Eb"},
              {"E": "E, F#, G#, B, C#, E"},
              {"F": "F, G, A, C, D, F"},
              {"F#": "F#, G#, A#, C#, D#, F#"},
              {"Gb": "Gb, Ab, Bb, Db, Eb, Gb"},
              {"G": "G, A, B, D, E, G"},
              {"Ab": "Ab, Bb, C, Eb, F, Ab"},
              {"A": "A, B, C#, E, F#, A"},
              {"Bb": "Bb, C, D, F, G, Bb"},
              {"B": "B, C#, D#, F#, G#, B"}]

minor_pent = [{"A": "A, C, D, E, G, A"},
              {"Bb": "Bb, Db, Eb, F, Ab, Bb"},
              {"B": "B, D, E, F#, A, B"},
              {"C": "C, Eb, F, G, Bb, C"},
              {"C#": "C#, E, F#, G#, B, C#"},
              {"D": "D, F, G, A, C, D"},
              {"Eb": "Eb, Gb, Ab, Bb, Db, Eb"},
              {"Em": "E, G, A, B, D, E"},
              {"F": "F, Ab, Bb, C, Eb, F"},
              {"F#m": "F#, A, B, C#, E, F#"},
              {"G": "G, Bb, C, D, F, G"},
              {"G#": "G#, B, C#, D#, F#, G#"}]

maj_or_min = input("Hello there. I'm a bot designed to output major or minor pentatonic scales based on user input. \nWould you like to start with major or minor? ")

if maj_or_min == "major":
    print("You picked major.")
    major_choice = input("\nI have all 12 major pentatonic scales in my database. Which one would you like to display? \n(Type the root note for the scale to choose - like C, C#, etc) ")
elif maj_or_min == "minor":
    print("You picked minor.")
    minor_choice = input("\nI have all 12 major pentatonic scales in my database. Which one would you like to display? \n(Type the root note for the scale to choose - like C, C#, etc) ")
else:
    print("You gave an incorrect input. Try again!")