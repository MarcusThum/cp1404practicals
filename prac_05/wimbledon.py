import csv

champions = []
countries = []
countries_dict = {}
champions_count = {}

with open('wimbledon.csv', "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        champions.append(row[2])
        countries.append(row[1])

    for champion in champions:
        champions_count[champion] = 0
        for compare_champion in champions:
            if compare_champion == champion:
                champions_count[champion] += 1

    champions_count.pop("Champion")

    for country in countries:
        countries_dict[country] = 0
        for compare_country in countries:
            if compare_country == country:
                countries_dict[country] += 1

    countries_dict.pop("Country")

    countries_collection = sorted([country for country in countries_dict.keys()])

    print("Wimbledon Champions:")
    for champion in champions_count.keys():
        print(f"{champion:18} {champions_count[champion]}")

    print("\n")
    print("These 12 countries have won Wimbledon:")
    print(f"{", ".join(countries_collection)}")
