def main():
    values = []

    while True:
        val = input("Enter a value: ")
        if val == "":
            break
        values.append(val)

    print("Here's the list:", values)

if __name__ == '__main__':
    main()
