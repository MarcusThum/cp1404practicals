colours = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALIZARIN CRIMSON": "#e32636", "AMARANTH": "#e52b50", "AMETHYST": "#9966cc", "AQUA": "#00ffff", "BAKER MILLER PINK": "#ff91af", "BANANA YELLOW": "#ffe135", "BARN RED": "#7c0a02", "BATTLESHIP GREY": "#848482"}

while True:
    user_input = input("Colour: ").upper()

    if user_input == "":
        break

    try:
        print(colours[user_input])
    except KeyError:
        print("Colour Not Stored")