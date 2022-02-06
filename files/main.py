import random,game
from classes import npc, player, weapon, room

'''
This class will run an instance of game.py
The game keeps running while the player is alive
'''

is_game_running = True
i=0

game_instance = game.game
game_instance.start_game()


def choose_room():
    room_of_choice = room.create_room()
    name_of_the_room = room_of_choice.getName()
    if name_of_the_room == "Abandoned house":
        print("In the outskirts, you found an abandoned house")
        print("Description:\n",room_of_choice.description)
    if name_of_the_room == "Old warehouse":
        print("After walking for hours, you reach the community center")
        print("Description:\n",room_of_choice.description)
    if name_of_the_room == "Metro":
        print("You decide to go to the metro see what lurks on the underground")
        print("Description:\n",room_of_choice.description)
    if name_of_the_room == "Military outpost":
        print("You reach the military outpost.")
        print("Description:\n",room_of_choice.description)
    if name_of_the_room == "Asylum":
        print("Almost leaving the city, there is the asylum. You decide to check it")
        print("Description:\n",room_of_choice.description)
    if name_of_the_room == "Mall":
        print("At the center of the city, there is a mall. You decide to loot it")
        print("Description:\n",room_of_choice.description)
    if name_of_the_room == "Bunker":
        print("During your exploration, you found a door to a bunker. God knows what you will find it there...")
        print("Description:\n",room_of_choice.description)

    
'''
Each room will have 4 enemies or only 1 boss.
'''
def generate_enemies():
    boss_presence = False
    enemies = []
    count = 0
    print("Your enemies in the room are:")
    while count < 4:
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
            count +=1
        
    






while is_game_running == True:
#while i < 6:
    '''
    while True, generate rooms and check if player is alive.
    '''

    name = game.player_instance.get_name()

    '''
    Choose the room
    '''
    choose_room()
    generate_enemies()

    '''
    When player leaves the room, see if he is alive
    '''
    player_current_hp = game.player_instance.get_current_hp()
    if player_current_hp <= 0:
        is_game_running = False
    if player_current_hp > 0:
        print("\nYou leave the room alive. You wander looking for a new spot.\n")
        key_pressed = input("Press Enter to continue")
        print("========================================")


    #i+=1
    

    