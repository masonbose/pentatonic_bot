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
    print("\nYou picked major.")
    print("I have all 12 major pentatonic scales in my database.")
    print("Which one would you like to display?") 
    major_choice = input("Type the root note (capital) for the scale to choose - like C, C#, etc): ")
    
    if major_choice == "C":
        print("The pentatonic scale for C is: C, D, E, G, A, C.")
    elif major_choice == "C#":
        print("The pentatonic scale for C# is: C#, D#, F, G#, A#, C#.")
    elif major_choice == "Db":
        print("The pentatonic scale for Db is: Db, Eb, F, Ab, Bb, Db.")
    elif major_choice == "D":
        print("The pentatonic scale for D is: D, E, F#, A, B, D.")
    elif major_choice == "Eb":
        print("The pentatonic scale for Eb is: Eb, F, G, Bb, C, Eb.")
    elif major_choice == "E":
        print("The pentatonic scale for E is: E, F#, G#, B, C#, E.")
    elif major_choice == "F":
        print("The pentatonic scale for F is: F, G, A, C, D, F.")
    elif major_choice == "F#":
        print("The pentatonic scale for F# is: F#, G#, A#, C#, D#, F#.")
    elif major_choice == "Gb":
        print("The pentatonic scale for Gb is: Gb, Ab, Bb, Db, Eb, Gb.")
    elif major_choice == "G":
        print("The pentatonic scale for G is: G, A, B, D, E, G.")
    elif major_choice == "Ab":
        print("The pentatonic scale for Ab is: Ab, Bb, C, Eb, F, Ab.")
    elif major_choice == "A":
        print("The pentatonic scale for A is: A, B, C#, E, F#, A.")
    elif major_choice == "Bb":
        print("The pentatonic scale for Bb is: Bb, C, D, F, G, Bb.")
    elif major_choice == "B":
        print("The pentatonic scale for Bb is: B, C#, D#, F#, G#, B.")
    else:
        print("That scale wasn't found. Try again: ")

elif maj_or_min == "minor":
    print("\nYou picked minor.")
    print("I have all 12 minor pentatonic scales in my database.")
    print("Which one would you like to display?")
    minor_choice = input("Type the root note (capital) for the scale to choose - like C, C#, etc): ")

    if minor_choice == "A":
        print("The pentatonic scale for A is: A, C, D, E, G, A.")
    elif minor_choice == "Bb":
        print("The pentatonic scale for Bb is: Bb, Db, Eb, F, Ab, Bb.")
    elif minor_choice == "B":
        print("The pentatonic scale for B is: B, D, E, F#, A, B.")
    elif minor_choice == "C":
        print("The pentatonic scale for C is: C, Eb, F, G, Bb, C.")
    elif minor_choice == "C#":
        print("The pentatonic scale for C# is: C#, E, F#, G#, B, C#.")
    elif minor_choice == "D":
        print("The pentatonic scale for D is: D, F, G, A, C, D.")
    elif minor_choice == "Eb":
        print("The pentatonic scale for Eb is: Eb, Gb, Ab, Bb, Db, Eb.")
    elif minor_choice == "Em":
        print("The pentatonic scale for Em is: E, G, A, B, D, E.")
    elif minor_choice == "F":
        print("The pentatonic scale for F is: F, Ab, Bb, C, Eb, F.")
    elif minor_choice == "F#m":
        print("The pentatonic scale for F#m is: F#, A, B, C#, E, F#.")
    elif minor_choice == "G":
        print("The pentatonic scale for G is: G, Bb, C, D, F, G.")
    elif minor_choice == "G#":
        print("The pentatonic scale for G# is: G#, B, C#, D#, F#, G#.")
    else:
        print("That scale wasn't found. Try again: ")
else:
    print("You gave an incorrect input. Try again!")

