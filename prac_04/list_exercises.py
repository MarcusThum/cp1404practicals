
NUM_OF_NUMBERS = 5
numbers = []

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

for number in range(1, NUM_OF_NUMBERS + 1):
    get_number = int(input(f"Number ({str(number)}): "))
    numbers.append(get_number)

print(f"The first number is {numbers[0:1][0]}")
print(f"The last number is {numbers[-1:][0]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers)}")

get_username = input("Username: ")
access_granted = bool(False)

for username in usernames:
    if get_username.lower() == username.lower():
        print("Access granted")
        access_granted = True

if(access_granted == False):
    print("Access denied")