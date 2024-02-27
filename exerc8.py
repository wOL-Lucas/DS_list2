

def is_perfect_number(number:int):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i

    return sum == number


number = int(input("Enter a number: "))
print(is_perfect_number(number))
