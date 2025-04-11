def main():
    counts = {}  

    while True:
        num = input("Enter a number: ")
        if num == "":
            break  
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    print()  # Blank line before results
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

if __name__ == "__main__":
    main()
