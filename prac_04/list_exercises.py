#Q  1.Basic list operations
numbers = []
NUMBERS_OF_INPUTS = 5

for i in range(NUMBERS_OF_INPUTS):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers)/len(numbers))



