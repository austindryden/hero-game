import random
from store import Potion, Sword, Armor, Shoes, Store
from battle import Battle
from hero import Character, Hero, Goblin, Zombie, Wizard, Necromancer, Archer, Shadow, class_map

def main():
    player = Hero("austin")
    store = Store()
    battle = Battle()
    playing = True
    win = None
    rounds = 0
    
    enemies = [Goblin, Zombie, Wizard, Necromancer, Archer, Shadow]
    while playing:
        player.status()
        displayTown()
        choice = int(input("make your selection "))
        if choice == 1:
            enemy = enemies[random.randint(0,5)]()
            win = battle.do_battle(player, enemy)
            if not win:
                playing = False
        if choice == 2:
            player.collectbounty()
            store.restock()
            if rounds > 10:
                store.restock(2)
            store.go_shopping(player)
        if choice == 3:
            player.useinventory()
        if choice == 4:
            print("Welcome to University!")
            print("select a new class")
            for key in class_map:
                print(f" {key}")
            new_class = input("select a class ")
            player = player.changeClass(new_class)
        if choice == 5:
            playing = False
    print("thanks for fighting")

def displayTown():
    print("1. GO FIGHT!")
    print("2. Go shopping.")
    print("3. inventory")
    print("4. university (change class)")
    print("4.leave")


main()