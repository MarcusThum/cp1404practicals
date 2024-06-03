import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
# Line 1 - Smallest 5, Largest 20
# Line 2 - Smallest 3, Largest 9 (Cannot Produce a 4)
# Line 3 - Smallest 2.5, Largest 5.5
"""

# Random number between 1 and 100 inclusive.
print(random.randint(1, 100))