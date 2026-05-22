import matplotlib.pyplot as plt
from collections import defaultdict


def pie_reviews_per_park(data):

    counts = defaultdict(int)

    for review in data:
        counts[review["Branch"]] += 1

    labels = list(counts.keys())
    values = list(counts.values())

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()


def bar_top_locations(data, park):

    locations = defaultdict(list)

    for review in data:
        if review["Branch"].lower() == park.lower():
            locations[review["Reviewer_Location"]].append(review["Rating"])

    averages = {}

    for location, ratings in locations.items():
        averages[location] = sum(ratings) / len(ratings)

    top10 = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:10]

    names = [item[0] for item in top10]
    values = [item[1] for item in top10]

    plt.bar(names, values)
    plt.xticks(rotation=45)
    plt.title("Top 10 Locations by Average Rating")
    plt.show()


def bar_avg_month_rating(data, park):

    months = defaultdict(list)

    for review in data:
        if review["Branch"].lower() == park.lower():
            month = review["Year_Month"].split("-")[1]
            months[month].append(review["Rating"])

    averages = {}

    for month, ratings in months.items():
        averages[month] = sum(ratings) / len(ratings)

    ordered = sorted(averages.items())

    labels = [item[0] for item in ordered]
    values = [item[1] for item in ordered]

    plt.bar(labels, values)
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title("Average Rating by Month")
    plt.show()