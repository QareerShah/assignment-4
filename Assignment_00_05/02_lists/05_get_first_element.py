def get_first_element(lst):
    # Print the first element of the list
    print("First element:", lst[0])

def main():
    elements = []

    count = int(input("How many elements will you enter? "))
    for i in range(count):
        item = input(f"Enter element #{i + 1}: ")
        elements.append(item)

    get_first_element(elements)

if __name__ == '__main__':
    main()



