from sys import argv

def main():
    if len(argv) == 1:
        return
    elif len(argv) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        try:
            elem = int(argv[1])
            if elem % 2 == 0:
                print("I'm even")
            else:
                print("I'm odd")
        except ValueError:
            print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main()