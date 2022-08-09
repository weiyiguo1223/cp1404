import random

NUMBERS_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


number_of_row = int(input("How many quick picks? "))
for i in range(number_of_row):
    row_numbers = []
    for j in range(NUMBERS_LINE):
        number = random.randint(MINIMUM_NUMBER,MAXIMUM_NUMBER)
        while number in  row_numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        row_numbers.append(number)
        print(number, end=" ")
    print()



