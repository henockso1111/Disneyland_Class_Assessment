import csv


def load_data(filename):

    data = []

    with open(filename, "r", encoding="latin-1") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Rating"] = int(row["Rating"])
            data.append(row)

    return data


def get_reviews_by_park(data, park):

    results = []

    for review in data:
        if review["Branch"].lower() == park.lower():
            results.append(review)

    return results


def count_reviews_by_location(data, park, location):

    count = 0

    for review in data:
        if review["Branch"].lower() == park.lower() and review["Reviewer_Location"].lower() == location.lower():
            count += 1

    return count


def average_rating_by_year(data, park, year):

    ratings = []

    for review in data:
        if review["Branch"].lower() == park.lower() and review["Year_Month"].startswith(year):
            ratings.append(review["Rating"])

    if len(ratings) == 0:
        return 0

    return sum(ratings) / len(ratings)