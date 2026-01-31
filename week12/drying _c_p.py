def yes_no_question(check):
    response = input(f"Is it {check}? (y/n)")

    if response.lower() == "y":
        return True
    return False


def drying_speed(is_sunny, is_windy):
    if is_sunny and is_windy:
        return "Fast"
    elif is_sunny or is_windy:
        return "Slow"
    return "not drying"

def dry_clothes():
    sunny = yes_no_question("sunny")
    windy = yes_no_question("windy")

    speed = drying_speed(sunny, windy)

    print(f"The drying status of your clothes is: {speed}")


if __name__ == "__main__":
    dry_clothes()



def explain(what, where):
    if what == "Monster" and where == "Bed":
        print("I'm friends with the monster that's under my bed.")
    elif what == "Doctor" and where == "Head":
        print("You're trying to save me, stop holding your breath.")
    else:
        print("You think I'm crazy, yeah, you think I'm crazy.")
explain("Monster", "Bed")
