class CoffeeMachine:
    water_C = 0
    milk_C = 0
    coffee_C = 0
    cups_C = 0
    money_C = 0
    run = False

    def __init__(self):
        self.water_C = 400
        self.milk_C = 540
        self.coffee_C = 120
        self.cups_C = 9
        self.money_C = 550
        self.run = True

    def use_machine(self):
        while self.run:
            self.selection(input("Write action (buy, fill, take, remaining, exit):"))

    def status(self):
        print()
        print("The coffee machine has:")
        print(str(self.water_C) + " of water")
        print(str(self.milk_C) + " of milk")
        print(str(self.coffee_C) + " of coffee beans")
        print(str(self.cups_C) + " of disposable cups")
        print(str(self.money_C) + " of money")
        print()

    def take(self):
        global money_C
        print("I Gave you $" + str(self.money_C))
        self.money_C = 0
        print()

    def fill(self):
        self.water_C += int(input("Write how many ml of water do you want to add:"))
        self.milk_C += int(input("Write how many ml of milk do you want to add:"))
        self.coffee_C += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups_C += int(input("Write how many disposable cups of coffee do you want to add:"))
        print()

    def buy(self, option):
        choice = int(option)
        if choice == 1:
            if self.water_C - 250 > 0:
                if self.coffee_C - 16 > 0:
                    if self.cups_C - 1 > 0:
                        print("I have enough resources, making you a coffee!")
                        self.water_C -= 250
                        self.coffee_C -= 16
                        self.cups_C -= 1
                        self.money_C += 4
                    else:
                        print("Sorry, not enough cups!")
                else:
                    print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough water!")

        if choice == 2:
            if self.water_C - 350 > 0:
                if self.milk_C - 75 > 0:
                    if self.coffee_C - 20 > 0:
                        if self.cups_C - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                            self.water_C -= 350
                            self.milk_C -= 75
                            self.coffee_C -= 20
                            self.cups_C -= 1
                            self.money_C += 7
                        else:
                            print("Sorry, not enough cups!")
                    else:
                        print("Sorry, not enough coffee beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")

        if choice == 3:
            if self.water_C - 200 > 0:
                if self.milk_C - 100 > 0:
                    if self.coffee_C - 12 > 0:
                        if self.cups_C - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                            self.water_C -= 200
                            self.milk_C -= 100
                            self.coffee_C -= 12
                            self.cups_C -= 1
                            self.money_C += 6
                        else:
                            print("Sorry, not enough cups!")
                    else:
                        print("Sorry, not enough coffee beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")

    def quit_coffee_machine(self):
        self.run = False

    def selection(self, choice):
        if choice == 'take':
            self.take()
        elif choice == 'fill':
            self.fill()
        elif choice == 'remaining':
            self.status()
        elif choice == 'exit':
            self.quit_coffee_machine()
        elif choice == 'buy':
            option_num = input("What do you want to buy?\n"
                               "1 - espresso,\n"
                               "2 - latte,\n"
                               "3 - cappuccino,\n"
                               "back - to main menu: ")
            if option_num in ['1', '2', '3']:
                self.buy(option_num)
        else:
            print("Unknown command")


machine = CoffeeMachine()
machine.use_machine()
