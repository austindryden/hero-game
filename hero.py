import random
stat_map = {"sword" : 'power', "armor": 'defense', "helmet": 'defense', "shoes": 'evade' }
class Character:
    def __init__(self,name, health, power, coins = 0, bounty = 0,speed = 10, inventory = []):
        self.name = name
        self.health = health
        self.maxhealth = health
        self.power = power
        self.coins = coins
        self.bounty = bounty
        self.bountyboard = 0
        self.defense = 0
        self.evade = 0
        self.speed = speed
        self.inventory = inventory
        self.equipment = {"sword": None, "armor": None, "helmet": None, "shoes":None}

    def changeClass(self, classtype):
        if classtype in class_map:
            self.unequip("sword")
            self.unequip("armor")    
            self.unequip("helmet")    
            self.unequip("shoes")    
            new_char = class_map[classtype](self.name, self.health, self.power, self.coins, self.bounty, self.inventory)
            return new_char
        else:
            print("no class exists!")
            return self


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

    def take_damage(self, dam):
        damage = (dam - self.defense)
        if (1 - 2.71**(-1*(self.evade/10))) > random.random():
            print(f"{self.name} evaded attack!")
        else:
            print(f"{self.name} have taken {damage} damage")
            self.health -= damage

    def is_alive(self):
        return (self.health > 0)

    def print_status(self):
        print(str(self))

    def collectbounty(self):
        self.coins += self.bountyboard
        self.bountyboard = 0

    def loot(self, victim):
        print("TIME TO LOOT THE CORPSE!")
        self.coins += victim.coins
        self.bountyboard += victim.bounty
        if victim.inventory != []:
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
    
    def unequip(self, item_slot):
        if item_slot in stat_map:
            if self.equipment[item_slot] != None:
                setattr(self, stat_map[item_slot], getattr(self, stat_map[item_slot]) - self.equipment[item_slot].value)        
                self.inventory.append(self.equipment[item_slot])
                self.equipment[item_slot] = None
    
    def equip(self, item):
        print(f'equipping {item.name} in {item.slot}')
        setattr(self, stat_map[item.slot], getattr(self, stat_map[item.slot]) + item.value)
        self.equipment[item.slot] = item

    

class Hero(Character):
    def __init__(self, name ="cecil", health = 10, power = 5, coins = 20, bounty = 0, speed = 2, inventory = []):
        super().__init__(name, health, power, coins, bounty, speed, inventory)

    def attack(self, victim):
        damage = self.power
        if 1 == random.randint(1,5):
            damage *= 1.2
        print(f"{self.name} attacks for {damage}")
        victim.take_damage(damage)
        if not victim.is_alive():
            print(f"{self.name} has killed {victim.name}")
            self.loot(victim)
    
class Goblin(Character):
    def __init__(self, name = "redcap", health = 6, power = 2, coins = 2, bounty = 6, speed = 10, inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)

class Zombie(Character):
    def __init__(self, name = "romero", health = 0, power = 2, coins = 0, bounty = 0, speed = 10, inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)
    
    def is_alive(self):
        return (self.health < 0)

class Medic(Character):
    def __init__(self, name = "florence", health = 10, power = 3, coins = 5, bounty = 10, speed =10, inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)

    def take_damage(self, dam):
        super().take_damage(dam)
        if self.health > 0 and (1 == random.randint(1,5)):
            self.health +=2

class Shadow(Character):
    def __init__(self, name = "kerrigan", health = 1, power = 3, coins = 0, bounty = 10, speed = 10, inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)

    def take_damage(self, dam):
        if (1 == random.randint(1,10)):
            super().take_damage(dam)

class Necromancer(Character):
    def __init__(self, name = "ordan", health = 8, power = 3, coins = 0, bounty = 0, speed = 10, inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)

    # def attack(self, victim):
    #    victim.take_damage(self.power)
    #    if not victim.is_alive():
    #        victim = zombie(victim.health, victim.power, victim.name)

class Archer(Character):
    def __init__(self, name = "orlando", health = 10, power = 4, coins = 0, bounty = 0, speed =10,inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)

class Wizard(Character):
    def __init__(self, name = "merlin", health = 8 , power = 1, coins = 0,  bounty = 6, speed = 10, inventory = []):
            super().__init__(name, health, power, coins, bounty, speed, inventory)

    def attack(self, victim):
        attack_power = self.power
        if (1 == random.randint(1,2)):
            print(f"{self.name} borrows your attack power!")
            attack_power = victim.power
        print(f"{self.name} attacks for {self.power}")
        victim.take_damage(attack_power)
        if not victim.is_alive():
           print(f"{self.name} has killed {victim.name}")
           self.loot(victim)


class_map = {"hero": Hero, "goblin": Goblin, "zombie": Zombie, "medic" : Medic, "shadow": Shadow, "necromancer": Necromancer, "archer": Archer, "wizard": Wizard}