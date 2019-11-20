class Item:
    def __init__(self, cost, name, value, attribute, slot = None):
        self.cost = cost
        self.name = name
        self.value = value
        self.attribute = attribute
        self.slot = slot

    def __str__(self):
        return f"{self.name}. Equip to increase {self.attribute} by {self.value}"

    def apply(self, char):
        char.unequip(self.slot)
        char.equip(self)

class Potion(Item):
    def __init__(self, cost =5, name= "potion", value = 2, attribute = "health"):
        super().__init__(cost, name, value, attribute)
        
    def apply(self, char):
        char.health += self.value
        if char.health > char.maxhealth:
            char.health = char.maxhealth
        print(f"{char.name}'s health has increased to {char.health}")

class Sword(Item):
    def __init__(self, cost =10, name= "iron sword", value = 2, attribute = "power", slot = "sword"):
        super().__init__(cost, name, value, attribute, slot)
    
    # def apply(self, char):
    #     char.unequip(self.slot)
    #     char.power += self.value
    #     char.equipment[self.slot] = self

class Armor(Item):
    def __init__(self, cost=10, name="leather armor", value=2, attribute = "defense", slot = "armor"):
        super().__init__(cost, name, value, attribute, slot)

    # def apply(self, char):
    #     char.unequip(self.slot)
    #     char.equip(self)

class Shoes(Item):
    def __init__(self, cost =10, name = "red shoes", value=2, attribute = "evade", slot = "shoes"):        
        super().__init__(cost, name, value, attribute, slot)

    # def apply(self, char):
    #     stat_map = {"sword" : self.power, "armor": self.defense, "helmet": self.defense, "shoes": self.evade }
    #     char.unequip(self.slot)
    #     stat_map[self.slot] += self.value
    #     char.equipment[self.slot] = self

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