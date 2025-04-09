def main():
    dividend : int = int(input("\033[1;3m Enter an integer to be divided: \033[0m"))
    divisor : int = int(input("\033[1;3m Enter an integer to divide by: \033[0m"))

    quotient : int = dividend // divisor
    reminder : int = dividend % divisor

    print(f"The result of this division is {quotient} with a reminder of {reminder}")


if __name__ == '__main__':
    main()