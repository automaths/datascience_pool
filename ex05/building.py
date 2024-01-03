from sys import argv


def building(val: str):
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0
    for i in val:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            punctuation += 1
    print(f"The text contains {len(val)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    if len(argv) == 1:
        val = input("What is the text to count?: ")
    elif len(argv) > 2:
        print("Too many arguments")
        return
    elif type(argv[1]) is not str:
        print("Argument must be a string")
        return
    else:
        val = argv[1]
    building(val)


if __name__ == "__main__":
    main()
