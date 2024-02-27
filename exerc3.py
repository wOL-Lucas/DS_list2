class Vending_machine:
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def sell(self):
        inserted_money = []
        while sum(inserted_money) < self.price:
            money = float(input("Insert money: "))
            if money > 0:
                inserted_money.append(money)


            if sum(inserted_money) == self.price:

                print("You have inserted enough money")
                break

            else:
                print("You have inserted: ", sum(inserted_money), "\nYou need more: ", self.price - sum(inserted_money))



vending_machine = Vending_machine("Coke", 2.50)
vending_machine.sell()
