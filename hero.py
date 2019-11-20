import random
class Character:
    def __init__(self,name, health, power, coins = 0, bounty = 0):
        self.name = name
        self.health = health
        self.maxhealth = health
        self.power = power
        self.coins = coins
        self.bounty = bounty
        self.bountyboard = 0
        self.defense = 0
        self.evade = 0
        self.inventory = []
        self.equipment = {"sword": None, "armor": None, "helmet": None, "shoes":None}
    
    def __str__(self):
        return f"{self.name} has {self.health} health and {self.power} power"

    def status(self):
        print(f"Character         : {self.name}")
        print(f"Coins             : {self.coins}")
        print(f"bounty to collect : {self.bountyboard}")
        print(f"health            : {self.health}/{self.maxhealth}")
        print(f"Attack Power      : {self.power}")
        print(f"defense           : {self.defense}")
        print(f"Evade             : {self.evade}")
        print(f"""Equipment         : Sword  : {self.equipment['sword']}""")
        print(f"""Equipment         : armor  : {self.equipment['armor']}""")
        print(f"""Equipment         : helmet : {self.equipment['helmet']}""")
        print(f"""Equipment         : shoes  : {self.equipment['shoes']}""")
    
    def attack(self, victim):
        print(f"{self.name} attacks for {self.power}")
        victim.take_damage(self.power)
        if not victim.is_alive():
            print(f"{self.name} has killed {victim.name}")
            self.loot(victim)

    def is_alive(self):
        return (self.health > 0)

    def print_status(self):
        print(str(self))

    def take_damage(self, dam):
        self.health -= (dam - self.defense)

    def collectbounty(self):
        self.coins += self.bountyboard
        self.bountyboard = 0

    def loot(self, victim):
        print("TIME TO LOOT THE CORPSE!")
        self.coins += victim.coins
        self.bountyboard += victim.bounty
        self.inventory.append(victim.inventory)
    
    def useinventory(self):
        if len(self.inventory) == 0:
            print("you have no inventory")
            return False
        print("0. Exit")
        for i in range(len(self.inventory)):
            print(f"{i+1}. {str(self.inventory[i])}")
        choice = int(input("make a selection : ")) - 1
        if (choice == -1):
            return False
        print(f"would you like to use {self.inventory[choice].name}")
        print("1 for Yes")
        print("2 for No")
        used = input("make a choice : ")
        if used != "1":
            return False
        print("using item")
        self.inventory.pop(choice).apply(self)
        return True

    # THIS IS PESUDOCODE! FLESH OUT METHOD BEFORE USE!
    # def changeClass(self, classtype):
            # dict1 = {"zombie": zombie} 
            # tuple_attributes = ()
            # new_guy = dict1["zombie"](tuple_attributes)

    #     if classtype == "ZOMBIE":
    #         new_char = zombie(self.all_my_passable_attributes)
    #     elif classtype == whatever_class:
    #         new_char = whatever_class(self.all_my_important_attributes)
    #     else:
    #         print('no such class!')


    #         return self
    #     return new_char

class Hero(Character):
    def __init__(self, name ="cecil", health = 10, power = 5, coins = 20, bounty = 0):
        super().__init__(name, health, power, coins, bounty)

    def attack(self, victim):
        if 1 == random.randint(1,5):
            print(f"{self.name} attacks for {self.power * 1.2}")
            victim.take_damage((self.power * 1.2))
        else:
            print(f"{self.name} attacks for {self.power}")
            victim.take_damage(self.power)
        if not victim.is_alive():
            print(f"{self.name} has killed {victim.name}")
            self.loot(victim)
    
class Goblin(Character):
    def __init__(self, name = "redcap", health = 6, power = 2, coins = 2, bounty = 6):
            super().__init__(name, health, power, coins, bounty)

class Zombie(Character):
    def __init__(self, name = "romero", health = 0, power = 2, coins = 0, bounty = 0):
            super().__init__(name, health, power, coins, bounty)
    
    def is_alive(self):
        return (self.health < 0)

class Medic(Character):
    def __init__(self, name = "florence", health = 10, power = 3, coins = 5, bounty = 10):
            super().__init__(name, health, power, coins, bounty)

    def take_damage(self, dam):
        super().take_damage(dam)
        if self.health > 0 and (1 == random.randint(1,5)):
            self.health +=2

class Shadow(Character):
    def __init__(self, name = "kerrigan", health = 1, power = 3, coins = 0, bounty = 10):
            super().__init__(name, health, power, coins, bounty)

    def take_damage(self, dam):
        if (1 == random.randint(1,10)):
            super().take_damage(dam)

class Necromancer(Character):
    def __init__(self, name = "ordan", health = 8, power = 3, coins = 0, bounty = 0):
            super().__init__(name, health, power, coins, bounty)

    # def attack(self, victim):
    #    victim.take_damage(self.power)
    #    if not victim.is_alive():
    #        victim = zombie(victim.health, victim.power, victim.name)

class Archer(Character):
    def __init__(self, name = "orlando", health = 10, power = 4, coins = 0, bounty = 0):
            super().__init__(name, health, power, coins, bounty)

class Wizard(Character):
    def __init__(self, name = "merlin", health = 8 , power = 1, coins = 0,  bounty = 6):
            super().__init__(name, health, power, coins, bounty)

    def attack(self, victim):
        attack_power = self.power
        if (1 == random.randint(1,2)):
            print(f"{self.name} steals your attack power!")
            attack_power = victim.power
        print(f"{self.name} attacks for {self.power}")
        victim.take_damage(attack_power)
        if not victim.is_alive():
           print(f"{self.name} has killed {victim.name}")
           self.loot(victim)