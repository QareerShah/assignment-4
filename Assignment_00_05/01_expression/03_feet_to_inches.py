INCHES_IN_FOOT : int = 12

def main():
    feet : float = float(input("\033[1;3m Enter number of feet: \033[0m"))

    inches : float = feet * INCHES_IN_FOOT

    print(f"That is {inches} inches!...")


if __name__ == '__main__':
    main()