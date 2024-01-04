from sys import argv


def sos(text: str):
    """
        Function that takes a string as an argument and encodes
        it into Morse Code.
        • The program supports space and alphanumeric characters
        • An alphanumeric character is represented by dots . and dashes -
        • Complete morse characters are separated by a single space
        • A space character is represented by a slash /
    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', ' ': '/'}
    morse_code = ''
    for letter in text:
        morse_code += morse_code_dict[letter.upper()] + ' '
    if len(morse_code) > 0:
        morse_code = morse_code[:-1]
    return morse_code


def main():
    if len(argv) != 2 or type(argv[1]) is not str:
        print('AssertionError')
        return
    print(sos(argv[1]))


if __name__ == '__main__':
    main()
