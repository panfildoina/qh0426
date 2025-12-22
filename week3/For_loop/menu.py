def show_menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")


def main_menu_loop():
    while True:  # program runs continuously
        show_menu()

        choice = input("\nEnter your choice: ").strip().upper()
        print(choice)   # this matches the example where input is printed

        # Confirm valid choices
        if choice == "A":
            print("You have chosen option A - View Data\n")

        elif choice == "B":
            print("You have chosen option B - Visualise Data\n")

        elif choice == "X":
            print("You have chosen option X - Exit")
            print("Exiting program... Goodbye!")
            break

        else:
            # Invalid choice
            print("Invalid choice! Please enter A, B, or X.\n")


# Run the menu
main_menu_loop()