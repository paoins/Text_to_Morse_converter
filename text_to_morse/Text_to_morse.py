# define each letter and it equivalent on morse
morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Inverse dictionary for  Morse-to-Text conversion
letter_dict = {value: key for key, value in morse_code_dict.items()}


def text_to_morse(text):
    '''

    converts text to morse code
    :param text: text to be converted
    :return: morse code
    '''
    text = text.upper()
    morse_code =' '.join(morse_code_dict.get(char,'?') for char in text)
    return morse_code

def morse_to_text(morse_code):
    '''
    converts morse code to text
    :param morse_code:  morse code to be converted
    :return: text of morse code
    '''
    morse_code = morse_code.split()
    word = ' '.join(letter_dict.get(char,'?') for char in morse_code)
    return word


name=input('Enter your name: ')
morse= text_to_morse(name)
print(morse)

text = morse_to_text(morse)
print(text)