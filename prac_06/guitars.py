from guitar import Guitar
def main():
    names = []
    years = []
    costs = []

    input_name = " "
    while input_name != "":
        try:
            input_name = input("Name: ")
            if input_name == "":
                break
            input_year = int(input("Year: "))
            input_cost = float(input("Cost: "))

            names.append(input_name)
            years.append(input_year)
            costs.append(input_cost)

            print(f"{input_name} ({input_year}) : ${input_cost} added")
        except ValueError:
            print("Value Error")

    print("... snip ...")
    print("\n")
    print("These are my guitars:")

    guitars_append = []
    count = 1
    guitars_append.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars_append.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    for i in guitars_append:
        print(f"Guitar {count}: {i}")
        count += 1

    for i in range(0, len(names)):
        guitars = Guitar(names[i], years[i], costs[i])
        if guitars.vintage_string() != "":
            print(f"Guitar {count + i}: {guitars} ({guitars.vintage_string()})")
        else:
            print(f"Guitar {count + i}: {guitars}")

main()