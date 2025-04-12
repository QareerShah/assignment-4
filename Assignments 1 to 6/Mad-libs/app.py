def mad_libs():
    print("let's play Mad Libs! fill in the blanks with your own words!")
    
    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Give me a funny adjective: ")
    random_object = input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action Verb: ")
    funny_exlamation = input("Give me a funny exclamation: ")

    story = f'''
    Once upon a time, {name} went to {place}. 
    There, they saw a {funny_adj} {random_object} 
    and a {animal} that loved to {action_verb}. 
    {name} couldn't help but shout, '{funny_exlamation}!'''

    print(f"\nHere is your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    mad_libs()