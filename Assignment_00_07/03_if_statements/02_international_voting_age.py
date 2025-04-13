def main():
    # Ask the user for their age
    age = int(input("How old are you? "))
    
    # Check voting eligibility in each country
    if age >= 16:
        print(f"You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print(f"You can vote in Stanlau where the voting age is 25.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print(f"You can vote in Mayengua where the voting age is 48.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is 48.")

if __name__ == '__main__':
    main()
