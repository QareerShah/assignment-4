ADULT_AGE = 18  # Legal adult age in the US

def is_adult(age):
    return age >= ADULT_AGE

def main():
    try:
        age = int(input("How old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
