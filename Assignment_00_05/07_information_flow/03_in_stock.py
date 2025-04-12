# Sample inventory
inventory = {
    "apple": 500,
    "banana": 200,
    "orange": 150,
    "pear": 1000,
    "grape": 300
}

def num_in_stock(fruit):
    return inventory.get(fruit.lower(), 0)  # returns 0 if fruit not found

def main():
    fruit = input("Enter a fruit: ").lower()
    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:\n")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
