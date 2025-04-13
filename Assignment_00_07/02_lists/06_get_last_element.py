def get_last_element(lst):
    # Print the last element of the list
    print("Last element:", lst[-1])

def main():
    elements = []

    count = int(input("How many elements will you enter? "))
    for i in range(count):
        item = input(f"Enter element #{i + 1}: ")
        elements.append(item)

    get_last_element(elements)

if __name__ == '__main__':
    main()
