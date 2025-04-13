# Constant for the maximum Fibonacci value
MAX_FIB_VALUE = 10000

def main():
    # Starting values
    a, b = 0, 1
    
    print("Fibonacci sequence up to", MAX_FIB_VALUE, ":")
    
    while a < MAX_FIB_VALUE:
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    main()
