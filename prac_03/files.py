# Question 1:
get_name = input("Name: ")
write_buffer = open('name.txt', 'w')
write_buffer.write(get_name)
write_buffer.close()

# Question 2:
read_buffer = open('name.txt', 'r')
read_name = read_buffer.read()
print(f"Hi, {read_name}!")

# Question 3:
with open('numbers.txt', 'r') as numbers:
    read = numbers.readlines()
    add = int()
    for i in range(0, 2):
        add += int(read[i])
    print(f"Result: {add}")

# Question 4:
with open('numbers.txt', 'r') as numbers:
    print(numbers.read())
