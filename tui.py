"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def main_menu():

    print("\nMAIN MENU")
    print("[A] Data Analysis")
    print("[B] Data Visualisation")
    print("[X] Exit")

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