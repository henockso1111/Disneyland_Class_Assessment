def main_menu():

    print("\nMAIN MENU")
    print("[A] Data Analysis")
    print("[B] Data Visualisation")
    print("[X] Exit")

    choice = input("Enter your choice: ")
    return choice.upper()


def submenu_a():

    print("\nDATA ANALYSIS MENU")
    print("[A] Show reviews for a park")
    print("[B] Number of reviews by location")
    print("[C] Average rating by year")

    choice = input("Enter your choice: ")
    return choice.upper()


def submenu_b():

    print("\nDATA VISUALISATION MENU")
    print("[A] Most reviewed parks")
    print("[B] Park ranking by nationality")
    print("[C] Most popular month by park")

    choice = input("Enter your choice: ")
    return choice.upper()

def submenu_a():

    print("\nDATA ANALYSIS MENU")
    print("[A] Show reviews for a park")
    print("[B] Number of reviews by location")
    print("[C] Average rating by year")
    print("[D] Average score per park by reviewer location")

    choice = input("Enter your choice: ")
    return choice.upper()