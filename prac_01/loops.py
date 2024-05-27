for i in range(1, 21, 2):
    print(i, end=' ')
print()

for f in range(0, 101, 10):
    print(f, end=' ')
print()

for u in range(20, 0, -1):
    print(u, end=' ')
print()

number_of_stars = int(input("Number of stars: "))

for t in range(0, number_of_stars + 1, 1):
    print("*" * t)