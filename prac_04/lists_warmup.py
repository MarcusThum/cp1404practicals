from typing import List

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
1. Change the first element of numbers to "ten" (the string, not the number 10)
2. Change the last element of numbers to 1
3. Print all the elements from numbers except the first two (slice)
4. Print whether 9 is an element of numbers
"""
print(["ten" for number in numbers])
numbers[-1:] = [1]
print(numbers)
print(numbers[2:])
print([bool(number) for number in numbers if number == 9])
