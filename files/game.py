from distutils.sysconfig import get_makefile_filename
import random
from classes import npc, player, room

'''
We start preparing an instance of the player class, so we can access the data from other files.
'''

player_instance = player.Player(None, 1000, 1000, 1)

number_of_rooms = 0
player_choose_room = False

class game():
    def start_game():
        player_name = input("What is your name?\n")
        print("So you are called " + player_name + " ?")
        confirmation = input("Y/N\n")
        confirmation = confirmation.upper()
        while confirmation != "Y":
            if confirmation == "N" or confirmation == "n":
                player_name = input("What is your name?\n")
                print("So you are called " + player_name + " ?")
                confirmation = input("Y/N\n")
                if confirmation.upper() == "Y":
                    break

        player_instance.set_nome(player_name)

        print("\n********************************************\n")
        print("Generating world...")
        print("\n********************************************\m")
        print("Welcome ", player_name, "\n")
        print("This is your current state:")
        print("Current HP: " + str(player_instance.current_hp))
        print("Max HP: " + str(player_instance.max_hp))
        print("First aid kits:" + str(player_instance.first_aid_kits))



    def combat(enemies):
        get_a_drop = random.randint(1,100)
        index = 1
        action = int(input(
                    "Choose your action:\n1- Attack an enemy\n2- Use item\n3 - See current HP\n"))
        for enemy in enemies:
                current_hp = enemy.get_hp()
                if current_hp <= 0:
                    enemies.remove(enemy)
                #LISTING ENEMIES
        if action == 1:
            #This block should be outside the if.
            if len(enemies) == 0:
                print("\nYou survived the room\n")
                if get_a_drop >= 70 and get_a_drop <= 100:
                    print("You found a first aid kit!\n")
                    player_instance.win_first_aid_kit()
                return

            print("Which enemy you will attack?")
            for e in enemies:
                print(str(index) + " - " + e.name + " - HP: ",e.hp)
                index += 1
            target_index = int(input())
            #ind = int(target_index)
            enemies[target_index-1].take_damage(10000)
            #player_instance.attack(target,1000)
        #game.combat(enemies)
        if action == 2:
            print("Heal")
            player_instance.heal()
        if action == 3:
            print("Current HP: ", player_instance.get_current_hp())
        game.combat(enemies)



    def generate_enemies():
        enemies = []
        count = 0
        print("You enter the room and find the following enemies:")
        while count < 2:
            enemy = npc.spawn_npc()
            enemy_is_boss = enemy.get_boss()
            if enemy_is_boss == True:
                enemies.clear()
                enemies.append(enemy)
                print(enemy.get_name())
                break
            else:
                enemies.append(enemy)
                print(enemy.get_name())
                count += 1
        game.combat(enemies)


    def choose_room():

        global player_choose_room

        room_of_choice = room.create_room()
        name_of_the_room = room_of_choice.getName()

        #name_of_the_room = "Abandoned house"

        if name_of_the_room == "Abandoned house":
            print("In the outskirts, you found an abandoned house")
            player_access_room = input("You want to check it?(Y/N)\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "Its just an ordinary house. It wouldnt worth the trouble checking it. Lets keep walking...\n\n")
                player_choose_room = False

            elif player_access_room == "Y" or player_access_room == "y":
                player_choose_room = True

        if name_of_the_room == "Old warehouse":
            print("After walking for hours, you reach the community center")
            player_access_room = input("You want to check it?(Y/N)\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "This warehouse is in bad shape. Lets find anything more interesting.\n\n")
                player_choose_room = False
            elif player_access_room == "Y" or player_access_room == "y":
                print("Description:\n", room_of_choice.description)
                player_choose_room = True

        if name_of_the_room == "Metro":
            print("You decide to go to the metro see what lurks on the underground")
            player_access_room = input("You want to check it?(Y/N)\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "You never heard about good things happening on the metro, only problems. Lets ignore it.\n\n")
                player_choose_room = False
            elif player_access_room == "Y" or player_access_room == "y":
                print("Description:\n", room_of_choice.description)
                player_choose_room = True
        if name_of_the_room == "Military outpost":
            print("You reach the military outpost.")
            player_access_room = input("You want to check it?(Y/N)\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "Since the outpost is a high value place, it was probably looted before. Not worth it.\n\n")
                player_choose_room = False
            elif player_access_room == "Y" or player_access_room == "y":
                print("Description:\n", room_of_choice.description)
                player_choose_room = True
        if name_of_the_room == "Asylum":
            print("Almost leaving the city, there is the asylum. You decide to check it")
            player_access_room = input("You want to check it?(Y/N)\n\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "A asylum in the middle of nowhere? Easy pass.\n")
                player_choose_room = False
            elif player_access_room == "Y" or player_access_room == "y":
                print("Description:\n", room_of_choice.description)
                player_choose_room = True
        if name_of_the_room == "Mall":
            print("At the center of the city, there is a mall. You decide to loot it")
            player_access_room = input("You want to check it?(Y/N)\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "You wonder how many thugs and monsters are living in a building so big. Probably not worth it.\n\n")
                player_choose_room = False
            elif player_access_room == "Y" or player_access_room == "y":
                print("Description:\n", room_of_choice.description)
                player_choose_room = True
        if name_of_the_room == "Bunker":
            print("During your exploration, you found a door to a bunker. God knows what you will find it there...")
            player_access_room = input("You want to check it?(Y/N)\n")
            if player_access_room == "N" or player_access_room == "n":
                print(
                    "An opportunity like this wont appear soon. But you value your love more than some loot.\n\n")
                player_choose_room = False
            elif player_access_room == "Y" or player_access_room == "y":
                print("Description:\n", room_of_choice.description)
                player_choose_room = True


    def check_if_player_is_alive():
        global number_of_rooms
        player_current_hp = player_instance.get_current_hp()
        if player_current_hp <= 0:
            print("GAME! OVER\nNumber of rooms you survived:", number_of_rooms)
            return False
        if player_current_hp > 0:
            print("\nYou leave the room alive. You wander looking for a new spot.\n")
            number_of_rooms += 1
            key_pressed = input("Press Enter to continue")
            print("\n========================================\n")
            return True