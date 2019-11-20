class Item:
    def __init__(self, cost, name, value, attribute):
        self.cost = cost
        self.name = name
        self.value = value
        self.attribute = attribute

    def __str__(self):
        return f"{self.name}. Equip to increase {self.attribute} by {self.value}"

class Potion(Item):
    def __init__(self, cost =5, name= "potion", value = 2, attribute = "health"):
        super().__init__(cost, name, value, attribute)
        
    def apply(self, char):
        char.health += self.value
        if char.health > char.maxhealth:
            char.health = char.maxhealth
        print(f"{char.name}'s health has increased to {char.health}")

class Sword(Item):
    def __init__(self, cost =10, name= "iron sword", value = 2, attribute = "power"):
        super().__init__(cost, name, value, attribute)
    
    def apply(self, char):
        if char.equipment["sword"] != None:
            char.power -= char.equipment["sword"].value
            char.inventory.append(char.equipment["sword"])
            char.equipment["sword"] = None
        
        char.power += self.value
        char.equipment["sword"] = self

class Armor(Item):
    def __init__(self, cost=10, name="leather armor", value=2, attribute = "defense"):
        super().__init__(cost, name, value, attribute)

    def apply(self, char):
        if char.equipment["armor"] != None:
            char.defense -= char.equipment["armor"].value
            char.inventory.appened(char.equipment["armor"])
            char.equipment["armor"] = None
        
        char.defense += self.value
        char.equipment["armor"] = self

class Shoes(Item):
    def __init__(self, cost =10, name = "red shoes", value=2, attribute = "evade"):        
        super().__init__(cost, name, value, attribute)

    def apply(self, char):
        if char.equipment["shoes"] != None:
            char.evade -= char.equipment["shoes"].value
            char.inventory.appened(char.equipment["shoes"])
            char.equipment["shoes"] = None
        
        char.evade += self.value
        char.equipment["shoes"] = self

class Store:
    name = "Olde Shoppe"
    items = [Potion(), Sword(), Armor(), Potion(25, "XPotion", 999)]

    def storefront(self):
        print(f"Welcome to {self.name}")
        print("take a look at our inventory")
        print("0. leave without buying anything")
        for i in range(len(self.items)):
            print(f"{i+1}. {self.items[i].name}, {self.items[i].cost} coins")
        
    def go_shopping(self, char):
        shopping = True
        while shopping:
            self.storefront()
            print(f"{char.name}, you have {char.coins} coins")
            choice = (int(input("make a selection "))-1)
            if choice == -1:
                shopping = False
            else:
                if char.coins < self.items[choice].cost:
                    print("you don't have enough money for that!")
                else:
                    char.coins -=self.items[choice].cost
                    char.inventory.append(self.items.pop(choice))
                
    def restock(self, level = 1):
        if level == 1:
            self.items = [Potion(), Sword(), Sword(2, "Buster Sword", 7), Armor(), Potion(25, "XPotion", 999)]
            self.name = "Olde Shoppe"