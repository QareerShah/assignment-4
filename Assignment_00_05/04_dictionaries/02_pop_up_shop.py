def main():
    fruits = {
        "apple": 5,
        "durian": 25,
        "jackfruit": 12.5,
        "kiwi": 6,
        "rambutan": 8,
        "mango": 10
    }

    total = 0

    for fruit in fruits:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total += quantity * fruits[fruit]

    print(f"\nYour total is ${total}")

if __name__ == "__main__":
    main()
