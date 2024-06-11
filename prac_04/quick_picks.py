import random

def main():

    lines = []

    num_of_lines = int(input("Enter Number of Lines: "))

    for line in range(1, num_of_lines + 1):

        lines = generate_line(lines)
        nums = check_duplicate(lines)

        while nums != []:
            nums = check_duplicate(lines)
            for num in nums:
                new_random_number = random.randint(1, 45)
                while lines[num] == new_random_number:
                    new_random_number = random.randint(1, 45)
                lines[num] = new_random_number

        lines = sorted(lines)

        for column in range(0, 6):
            print(f"{lines[column]:2}", end=" ")
        print()

        lines = []
        nums = []


def generate_line(lines):
    for column in range(1, 7):
        lines.append(random.randint(1,45))

    return sorted(lines)

def check_duplicate(lines):
    nums = []
    for line in range(0, len(lines)):
        for num in range(0, len(lines)):
            if(line != num):
                if lines[line] == lines[num]:
                    nums.append(num)

    return nums

main()
