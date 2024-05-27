def main():
    score = float()
    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Error: Outside of Range")
        score = float(input("Enter score: "))
    return score

def show_stars(score):
    if(score > 0):
        print("*" * score)

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
