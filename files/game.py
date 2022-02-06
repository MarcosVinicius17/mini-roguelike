import random
from classes import npc, player, room_old, weapon

'''
This class is responsible for doing the interaction between player and game. Fights, going to another place, etc.
'''
'''
Prepare an instance of the player class, so we can access the data from other files.
'''

player_instance = player.Player(None,1,1000,1000,0,[],1000)


class game():
    def start_game():
        player_name = input("What is your name?\n")
        print("So you aDre called " + player_name +" ?")
        confirmation = input("Y/N\n")
        confirmation = confirmation.upper()
        while confirmation != "Y":
            if confirmation == "N" or confirmation == "n":
                player_name = input("What is your name?\n")
                print("So you are called " + player_name +" ?")
                confirmation = input("Y/N\n")
                if confirmation.upper() == "Y":
                    break
            #Make sure the inputs are only "Y" or "N"
            '''else:
                print("Please, i only accept the values 'Y' or 'N'")'''


        player_instance.set_nome(player_name)

        #After the player choose his name, we create the world and show his stats 
        print("Generating world...")

        #Create the starter items
        starter_knife = weapon.Weapon("Starter knife",20,0.05,"Ranged")
        old_revolver = weapon.Weapon("Old revolver",25,0.10,"Ranged")

        
        #player_char = player.Player(player_name,1,1000,1000,0,[],1000)

        print("This is your current state:")
        print("Name: " + player_instance.name)
        print("Max HP: " + str(player_instance.max_hp))
        print("Current HP: " + str(player_instance.current_hp))
        print("Skill points: " + str(player_instance.skill_points))
        #We need to create the items first. So for now, the inventory is empty
        print("Inventory: Your inventReory is empty")
        print("Money: " + str(player_instance.money ))

        print("Tip:You can always type !stats to see your stats")

''' def create_thug():
        thug = npc.NPC("Thug",1200,50,True,[])
        return thug'''

