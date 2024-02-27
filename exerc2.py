_numbers = []

number = int(input("Enter a number: "))
while number > 0:
    _numbers.append(number)
    number = int(input("Enter a number: "))

print("Sum of numbers: ", sum(_numbers), "\nAverage of the numbers: ", sum(_numbers) / len(_numbers))

