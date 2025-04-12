import random

def main():
    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=' ')
    print()  # Newline at the end

# Run the function
if __name__ == "__main__":
    main()
