from process import load_data, get_reviews_by_park, count_reviews_by_location, average_rating_by_year
from tui import main_menu, submenu_a, submenu_b
from visual import pie_reviews_per_park, bar_top_locations, bar_avg_month_rating


def main():
    print("DISNEYLAND REVIEW ANALYSIS SYSTEM")
    print("---------------------------------")

    # Load dataset
    data = load_data("Disneyland_reviews.csv")

    print("Dataset loaded successfully.")
    print(f"Number of reviews: {len(data)}")

    # Main program loop
    while True:
        choice = main_menu()
        print(f"You selected option {choice}")

        if choice == "A":

            sub_choice = submenu_a()

            if sub_choice == "A":
                park = input("Enter park name: ")
                reviews = get_reviews_by_park(data, park)

                for review in reviews:
                    print(review)

            elif sub_choice == "B":
                park = input("Enter park name: ")
                location = input("Enter reviewer location: ")

                count = count_reviews_by_location(data, park, location)
                print(f"{count} reviews found.")

            elif sub_choice == "C":
                park = input("Enter park name: ")
                year = input("Enter year (YYYY): ")

                avg = average_rating_by_year(data, park, year)
                print(f"Average rating: {avg}")

        elif choice == "B":

            sub_choice = submenu_b()

            if sub_choice == "A":
                pie_reviews_per_park(data)

            elif sub_choice == "B":
                park = input("Enter park name: ")
                bar_top_locations(data, park)

            elif sub_choice == "C":
                park = input("Enter park name: ")
                bar_avg_month_rating(data, park)

        elif choice == "X":
            print("Exiting program...")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()