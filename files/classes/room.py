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

    def getName(self):
        return self.name
    
        
abandoned_house_dict = {
    "name": "Abandoned house",
    "description": "An abandoned house who somehow managed to stay in one piece. Not a proper place to live, but is better than living outside."
}


old_warehouse_dict = {
    "name": "Old warehouse",
    "description": "A warehouse located in the outskirts. It has boxes of all kinds, maybe you can scavenge something valuable."
}

metro_dict = {
    "name": "Metro",
    "description": "A metro station. It was filled with people before the war, not its just a dark and empty place filled with dangers."
}


military_outpost_dict = {
    "name": "Military outpost",
    "description": "A outpost created to protect important facilities. The people inside didn’t last much, but the structures still solid."

}

asylum_dict = {
    "name": "Asylum",
    "description": "An abandoned and scary place. You think if getting some loot worth the risk of getting nightmares."
}


community_center_dict = {
    "name": "Community center",
    "description": "A big building to help the civilians. The big number of people ended up overwhelming the place, but now, there is no one left."
}

mall_dict = {
    "name": "Mall",
    "description": "A big building in good condition with all kind of stores. This is probably a good place to loot, but also a good place to find trouble."
}


bunker_dict = {
    "name" : "Bunker",
    "description": "A military emergency bunker, made when things got tough. Of course, a valiable facility will attract the worst kind of people, but they also have the better loot..."
}



'''Pick a random room from rooms_list, generate some random room and a list of enemies inside. Dont forget about the chance of being a non hostile room.'''
'''
    The odds are: house = 20%, warehouse = 20%, metro = 10%, 
    military outpost = 5%, asylum = 10%,community center = 
    20%, mall = 10%, bunker = 5%
    '''
def create_room():

    room_index = random.randint(1,100)
    if room_index < 20:
        abandoned_house = room(abandoned_house_dict["name"],abandoned_house_dict["description"])
        return abandoned_house
    if room_index >= 20 and room_index <= 39:
        old_warehouse = room(old_warehouse_dict["name"],old_warehouse_dict["description"])
        return old_warehouse
    if room_index >=40 and room_index <=49:
        metro = room(metro_dict["name"],metro_dict["description"])
        return metro
    if room_index >=50 and room_index <=54:
        military_outpost = room(military_outpost_dict["name"], military_outpost_dict["description"])
        return military_outpost
    if room_index >=55 and room_index <= 64:
        asylum = room(asylum_dict["name"],asylum_dict["description"])
        return asylum
    if room_index >=65 and room_index <= 84:
        community_center = room(community_center_dict["name"], community_center_dict["description"])
        return community_center
    if room_index >= 85 and room_index <= 94:
        mall = room(mall_dict["name"],mall_dict["description"])
        return mall
    if room_index >=95 and room_index <=100:
        bunker = room(bunker_dict["name"], bunker_dict["description"])
        return bunker 
