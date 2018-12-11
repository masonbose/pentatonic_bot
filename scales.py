#!/usr/bin/python3
def ask_scale():
    retry = 0
    valid_scale = False
    print('\nHey there. I am a bot designed to output major or minor pentatonic scales based on user input.')
    while not valid_scale:
        response = input('[M]ajor or [m]inor scale? ')
        if response.startswith('M'):
            valid_scale = True
            scale = 'major'
        elif response.startswith('m'):
            valid_scale = True
            scale = 'minor'
        else:
            retry += 1
            if retry > 4:
                raise SystemExit('Invalid scales entered. Too many retries.')
    return response[0]


def pentatonic(scale):
    retry = 0
    valid_root = False
    pentatonic_scales = {
        'MC': ['C', 'D', 'E', 'G', 'A', 'C'],
        'MC#': ['C#', 'D#', 'F', 'G#', 'A#', 'C#'],
        'MDb': ['Db, Eb, F, Ab, Bb, Db'],
        'MD': ['D, E, F#, A, B, D'],
        'MEb': ['Eb, F, G, Bb, C, Eb'],
        'ME': ['E, F#, G#, B, C#, E'],
        'MF': ['F, G, A, C, D, F'],
        'MF#': ['F#, G#, A#, C#, D#, F#'],
        'MGb': ['Gb, Ab, Bb, Db, Eb, Gb'],
        'MG': ['G, A, B, D, E, G'],
        'MAb': ['Ab, Bb, C, Eb, F, Ab'],
        'MA': ['A, B, C#, E, F#, A'],
        'MBb': ['B, C, D, F, G, Bb'],
        'MB': ['B, C#, D#, F#, G#, B'],
        'mA': ['A, C, D, E, G, A'],
        'mBb': ['Bb, Db, Eb, F, Ab, Bb'],
        'mB': ['B, D, E, F#, A, B'],
        'mC': ['C, Eb, F, G, Bb, C'],
        'mC#': ['C#, E, F#, G#, B, C#'],
        'mD': ['D, F, G, A, C, D'],
        'mEb': ['Eb, Gb, Ab, Bb, Db, Eb'],
        'mEm': ['E, G, A, B, D, E'],
        'mF': ['F, Ab, Bb, C, Eb, F'],
        'mF#': ['F#, A, B, C#, E, F#'],
        'mG': ['G, Bb, C, D, F, G'],
        'mG#': ['G#, B, C#, D#, F#, G#']}

    print('Choose a root note. Add "#" for sharps, "b" for flats, or "-m" for minors.')
    while not valid_root:
        response = input("Note? ")
        root_note = response[0].upper()
        if root_note in 'ABCDEFG':
            sharp = 1 if '#' in response[1:] else 0
            flat = 1 if 'b' in response[1:] else 0
            full_scale = '{}{}{}'.format(
                scale, root_note, '#' * sharp + 'b' * flat)
            notes = pentatonic_scales.get(full_scale)
            if notes:
                valid_root = True
                print('{} pentatonic scale for {} is {}'.
                      format('Major' if scale == 'M' else 'Minor',
                             full_scale[1:],
                             ', '.join(notes)))
            else:
                retry += 1
                print('{} pentatonic scale {} not found.'.format(
                    'Major' if scale == 'M' else 'Minor', full_scale[1:]))
                if retry > 4:
                    raise SystemExit('Invalid scale. Too many retries.')


def main():
    scale = ask_scale()
    pentatonic(scale)


if __name__ == '__main__':
    main()
