def main():
    length_password = get_password()
    print("*" * length_password)

def get_password():
    get_password = input("Password (Length: 5 Words): ")
    length_of_password = len(get_password)
    while length_of_password < 5:
        print("Error: Minimum Word Length 5 Words")
        get_password = input("Password (Length: 5 Words): ")
        length_of_password = len(get_password)
    return length_of_password

main()


