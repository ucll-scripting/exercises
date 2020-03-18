to_morse_table = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..' }

from_morse_table = dict( (y, x) for x, y in to_morse_table.items() )


def to_morse(string):
    return '   '.join( [ ' '.join( [ to_morse_table[char] for char in word ] ) for word in string.upper().split(' ') ] )

def from_morse(string):
    return ' '.join( [ ''.join( [ from_morse_table[char] for char in word.split(' ') ] ) for word in string.split('   ') ] )