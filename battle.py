import random

class Battle:
    def do_battle(self, char, enemy):
        defending = False
        flee = False
        print("TIME TO FIGHT!")
        print(f"{char.name} Vs. {enemy.name}")
        while char.is_alive() and enemy.is_alive() and not flee:
            flee = False
            self.battle_menu()
            choice = int(input("make a selection : "))
            if choice == 1:
                char.attack(enemy)
            if choice == 2:
                defending = True
            if choice == 3:
                if not char.useinventory():
                    continue
            if choice == 4:
                fleeChance = random.randint(1,2)
                if fleeChance == 1:
                    print("sorry flee attempt failed")
                else:
                    print("you have fled the battle.")
                    return True
            if enemy.is_alive():
                if defending:
                    char.armor += 2
                    enemy.attack(char)
                    char.armor -= 2
                else:
                    enemy.attack(char)
            if not char.is_alive():
                print("you have perished")
                return False
            if not enemy.is_alive():
                print("you have prevailed!")
                return True

    def battle_menu(self):
        print("Battle Menu")
        print("1. Attack!")
        print("2. defend")
        print("3. inventory")
        print("4. flee")