import random
from store import Potion, Sword, Armor, Shoes, Store
from battle import Battle
from hero import Character, Hero, Goblin, Zombie, Wizard, Necromancer, Archer, Shadow

def main():
    player = Hero("austin")
    store = Store()
    battle = Battle()
    playing = True
    win = None
    
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
            store.go_shopping(player)
        if choice == 3:
            player.useinventory()
        if choice == 4:
            playing = False
    print("thanks for fighting")

def displayTown():
    print("1. GO FIGHT!")
    print("2. Go shopping.")
    print("3. inventory")
    print("4.leave")

main()