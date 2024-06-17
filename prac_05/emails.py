name_email_dict = {}

while True:
    email = input("Email: ")

    if email == "":
        break

    name = email.split("@")[0]

    check_name = input(f"Is your name {name}? (y/n) ").lower()

    while check_name != "y" and check_name != "n":
        check_name = input(f"Is your name {name}? (y/n) ").lower()

    if check_name == "y":
        name_email_dict[email] = name
    elif check_name == "n":
        input_name = input("Name: ")
        name_email_dict[email] = input_name

    print(name_email_dict)

print("\n")
for email in name_email_dict.keys():
    print(f"{name_email_dict[email]} ({email})")



