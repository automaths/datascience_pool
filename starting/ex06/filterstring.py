from sys import argv


def filterstring(text: str, length: int):
    """
        Function that accepts two arguments: a string(S), and an integer(N).
        The program should output a list of words from S that have a length
        greater than N.
            • Words are separated from each other by space characters.
            • Strings do not contain any special characters.
              (Punctuation or invisible)
    """
    return [x for x in text.split(' ') if len(x) > length]


def main():
    if len(argv) != 3 or not argv[2].isdigit() or not type(argv[1]) is str:
        print("AssertionError: the arguments are bad")
        return
    print(filterstring(argv[1], int(argv[2])))


if __name__ == "__main__":
    main()
