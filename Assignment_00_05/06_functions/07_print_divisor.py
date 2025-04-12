def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()  # Adds a newline at the end

def main():
    number = int(input("Enter a number: "))
    print_divisors(number)

if __name__ == "__main__":
    main()
