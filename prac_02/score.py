"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    get_print_score()
def get_print_score():
    score = float(input("Enter score: "))
    print(result(score))

def result(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score < 100:
        return "Excellent"
    else:
        return "Invalid score"

main()

