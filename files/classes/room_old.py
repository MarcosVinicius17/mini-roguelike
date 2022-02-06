'''
This is a room. They are the locations of the game, where the player will find itens, enemies and friendly npcs.
Each room will have a set of enemies and some items like ammo or money.
There is also a small chance of the room having a trader and no enemies.
'''
import random

class room():
    def __init__(self,name,description):
        self.name = name
        self.description = description

    
        
abandoned_house = {
    "name": "Abandoned house",
    "description": "An abandoned house who somehow managed to stay in one piece. Not a proper place to live, but is better than living outside."
}


old_warehouse = {
    "name": "Old warehouse",
    "description": "A warehouse located in the outskirts. It has boxes of all kinds, maybe you can scavenge something valuable."
}

metro = {
    "name": "Metro",
    "description": "A metro station. It was filled with people before the war, not its just a dark and empty place filled with dangers."
}


military_outpost = {
    "name": "Military outpost",
    "description": "A outpost created to protect important facilities. The people inside didn’t last much, but the structures still solid."

}

asylum = {
    "name": "Asylum",
    "description": "An abandoned and scary place. You think if getting some loot worth the risk of getting nightmares."
}


community_center = {
    "name": "Community center",
    "description": "A big building to help the civilians. The big number of people ended up overwhelming the place, but now, there is no one left."
}

mall = {
    "name": "Mall",
    "description": "A big building in good condition with all kind of stores. This is probably a good place to loot, but also a good place to find trouble."
}


bunker = {
    "name" : "Bunker",
    "description": "A military emergency bunker, made when things got tough. Of course, a valiable facility will attract the worst kind of people, but they also have the better loot..."
}

rooms_list = [abandoned_house,old_warehouse,metro,military_outpost,asylum, community_center, mall, bunker]

bunker = room("Bunker","A military emergency bunker, made when things got tough. Of course, a valiable facility will attract the worst kind of people, but they also have the better loot...")




'''Pick a random room from rooms_list, generate some random room and a list of enemies inside. Dont forget about the chance of being a non hostile room.'''
def create_room():
    print("Generating room...")
    room_of_choice = random.choice(rooms_list)
    print("The room is : " + room_of_choice["name"])
    '''
    Already got the room, now we need to populate her.
    '''

'''def generate_npcs():
    thug = npc.NPC("Thug",1000,50,True,[])'''
