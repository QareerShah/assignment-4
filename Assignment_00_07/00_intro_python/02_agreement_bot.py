            #    we use (ANSI Escape) for bold and etalic

def main():

    animal = input("\033[1;3m What's your favorite animal_____? \033[0m")    # here we use (ANSI Escape)
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    main()