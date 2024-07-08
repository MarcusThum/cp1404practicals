from guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(gibson_guitar)
print("\n")
print(f"{gibson_guitar.name} get_age() - Expected {2024 - gibson_guitar.year} Got {gibson_guitar.get_age()}")
print(f"{gibson_guitar.name} is_vintage() - Expected {2024 - gibson_guitar.year >= 50} Got {gibson_guitar.is_vintage()}")

print("\n")

another_guitar = Guitar("Another Guitar", 2013, 16035.40)

print(f"{another_guitar.name} get_age() - Expected {2024 - another_guitar.year} Got {another_guitar.get_age()}")
print(f"{another_guitar.name} is_vintage() - Expected {2024 - another_guitar.year >= 50} Got {another_guitar.is_vintage()}")
