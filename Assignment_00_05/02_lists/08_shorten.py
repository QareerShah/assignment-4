MAX_LENGTH = 3  

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove item from the end of the list
        print(removed_item)  # Print the item removed

def main():
    values = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    print("Original list:", values)
    
    shorten(values)
    
    print("Modified list:", values)

if __name__ == '__main__':
    main()
