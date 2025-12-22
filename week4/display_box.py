def display_box(word):
    num_dashes = 4 +len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)

def display_lower_case(word):
    print(word.lower())

def display_uupper_case(word):
    print(word.upper())

def display_mirrored(word):
    mirror=""
    for letter in reversed(word):
        mirror += letter
    print(f"{word} | {mirror}")

def  dispaly_repeated(word):
    repetitions = int(input("How many times should the word display "))

    for repetitions in range(repetitions):
        if (repetitions % 2 ==0):
            print(display_lower_case(word))
        else:
            print(display_lower_case(word))

def run():
    word= input("Please enter a word")

 is_looping = True

 while(is_looping):
    print("Please select a option:")
    print("[1] Display in a box")
    print("[2] Display lowe case")
    print("[3] Display upper case")
    print("[4] Display mirrored")
    print("[5] Display repeated")
    print("[6] Exit")

    response = int(input())

    if response == 1:
         display_box(word)
    elif response == 2:
         display_lower_case(word)
    elif response == 3:
        display_uupper_case(word)
    elif response == 4:
       display_mirrored(word)
    elif response == 5:
       display_repeated(word)
    else:
       print("Unknown option...")

run()
