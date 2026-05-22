def verify_age():
    age = int(input("Enter age: "))
    if age >= 18:
        return 'Adult'
    else:
        return 'Child'


def child_menu():
    print("1: Decaf Black coffee")
    print("2: Decaf White coffee")
    print("3: Exit")


def adult_menu():
    print("1: Black coffee")
    print("2: White coffee")
    print("3: Exit")


user_type = verify_age()

while True:
    if user_type == "Adult":
        adult_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Black coffee selected")
        elif choice == 2:
            print("White coffee selected")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

    else:
        child_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Decaf Black coffee selected")
        elif choice == 2:
            print("Decaf White coffee selected")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice")