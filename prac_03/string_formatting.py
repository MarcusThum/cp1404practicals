"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# TODO: Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,036!
print(f"{year} {name} for about {cost:.0f}")

# TODO: Using a for loop with the range function and f-string formatting,
# produce the following right-aligned output (DO NOT use a list):

for i in range(0, 11):
    print(f"2 ^ {i} is  {2**i}")