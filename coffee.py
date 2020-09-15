class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    disposable_cups = 9
    money = 550
    
    def __init__(self, choice):
        self.choice = choice
        self.espresso_water = 250
        self.espresso_beans = 16
        self.espresso_money = 4

        self.latte_water = 350
        self.latte_milk = 75
        self.latte_beans = 20
        self.latte_money = 7

        self.cappucino_water = 200
        self.cappucino_milk = 100
        self.cappucino_beans = 12
        self.cappucino_money = 6
    
    def buy(self):
        if self.choice == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            coffee = input()
            
            if coffee == "1":
                if CoffeeMachine.water < self.espresso_water:
                    print("Sorry, not enough water!")
                elif CoffeeMachine.beans < self.espresso_beans:
                    print("Sorry, not enough beans!")
                elif CoffeeMachine.disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    CoffeeMachine.water -= self.espresso_water
                    CoffeeMachine.beans -= self.espresso_beans
                    CoffeeMachine.money += self.espresso_money
                    CoffeeMachine.disposable_cups -= 1
                    print("I have enough resources, making you a coffee!")
            
            elif coffee == "2":
                if CoffeeMachine.water < self.latte_water:
                    print("Sorry, not enough water!")
                elif CoffeeMachine.milk < self.latte_milk:
                    print("Sorry, not enough milk!")
                elif CoffeeMachine.beans < self.latte_beans:
                    print("Sorry, not enough beans!")
                elif CoffeeMachine.disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    CoffeeMachine.water -= self.latte_water
                    CoffeeMachine.milk  -= self.latte_milk
                    CoffeeMachine.beans -= self.latte_beans
                    CoffeeMachine.money += self.latte_money
                    CoffeeMachine.disposable_cups -= 1
                    print("I have enough resources, making you a coffee!")
            
            elif coffee == "back":
                print("Taking you back to the main menu :)")
                print()

            else:
                if CoffeeMachine.water < self.cappucino_water:
                    print("Sorry, not enough water!")
                elif CoffeeMachine.milk < self.cappucino_milk:
                    print("Sorry, not enough milk!")
                elif CoffeeMachine.beans < self.cappucino_beans:
                    print("Sorry, not enough beans!")
                elif CoffeeMachine.disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    CoffeeMachine.water -= self.cappucino_water
                    CoffeeMachine.milk  -= self.cappucino_milk
                    CoffeeMachine.beans -= self.cappucino_beans
                    CoffeeMachine.money += self.cappucino_money
                    CoffeeMachine.disposable_cups -= 1
                    print("I have enough resources, making you a coffee!")
            
    def fill(self):
        if self.choice == "fill":
            print("Write how many ml of water do you want to add:")
            CoffeeMachine.water += int(input())
            print("Write how many ml of milk do you want to add:")
            CoffeeMachine.milk += int(input())
            print("Write how many grams of coffee beans do you want to add:")
            CoffeeMachine.beans += int(input())
            print("Write how many disposable cups of coffee do you want to add:")
            CoffeeMachine.disposable_cups += int(input())

    def take(self):
        if self.choice == "take":
            print(f"I gave you {CoffeeMachine.money}")
            CoffeeMachine.money = 0

    def remaining(self):
        if self.choice == "remaining":
            print(f"""The coffee machine has:
        {CoffeeMachine.water} of water
        {CoffeeMachine.milk} of milk
        {CoffeeMachine.beans} of coffee beans
        {CoffeeMachine.disposable_cups} of disposable cups
        ${CoffeeMachine.money} of money""")

#End Of CoffeeMachine Class..............    

def mainmenu():
    global condition
    print("Write action (buy, fill, take, remaining, exit):")
    choice = input()

    if choice == "exit":
        condition = False

    coffee = CoffeeMachine(choice)
    coffee.buy()
    coffee.fill()
    coffee.take()
    coffee.remaining()

condition = True
while condition:
    mainmenu()