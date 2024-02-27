
def generate_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

choosen_number = input("Enter a number: ")
generate_table(int(choosen_number))
