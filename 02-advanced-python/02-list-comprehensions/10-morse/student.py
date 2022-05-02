# Write your code here
def to_morse(string):
    words = string.split(' ')
    morsearray = []
    for letters in words:
        lettersarray = list(letters)
        morseletterarray = []
        for letter in lettersarray:
            morseletter = morsecode[letter.upper()]
            morseletterarray.append(morseletter)
        result = (' ').join(morseletterarray)
        morsearray.append(result)
    return ('   ').join(morsearray)
        
    ###    words = [sdds sdsd sdsds]
    ###    morsearray = []
    ###    letters = "sdds"
    ###    lettersarray = ['s','d','d','d']
    
    ###    letter = 's'
    ###    morseletter = "..."
    ###    morseletterarray = ['.. ','...',]
    ###    result = "... ... .. .."
    ###    morsearray = [" .. .. .. ..", ".. .. .. .."]
def from_morse(string):
    words = string.split('   ')
    morsearray = []
    for letters in words:
        lettersarray = letters.split(' ')
        morseletterarray = []
        for letter in lettersarray:
            morseletter = morsecodereverse[letter]
            morseletterarray.append(morseletter.upper())
        result = ('').join(morseletterarray)
        morsearray.append(result)
    return (' ').join(morsearray)

    ###    words = [... .. ....,...,....,....]
    ###    morsearray = []
    ###    letters = "... .... ..."
    ###    lettersarray = ['...','...','..']
    
    ###    letter = '...'
    ###    morseletter = "s"
    ###    morseletterarray = ['S','A',]
    ###    result = "SA"
    ###    morsearray = ["SA", "LOL"]

morsecode = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":"."	,
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-"	,
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--.."
} 

morsecodereverse = dict((y,x) for (x,y) in morsecode.items())
