import random
class NPC():
    def __init__(self,name,description,hp,attack,hostile,inventory,boss):
        self.name = name
        self.description = description
        self.hp = hp
        self.attack = attack
        self.hostile = hostile
        self.inventory = inventory
        self.boss = boss

    def get_boss(self):
        return self.boss

    def get_name(self):
        return self.name
        
    def get_hp(self):
        return self.hp
        
    def get_attack(self):
        return self.attack

    def get_hostile(self):
        return self.hostile

    def get_inventory(self):
        return self.inventory

    def check_inventory(self):
        for i in self.inventory:
            print(self.inventory[i] + " - ")

    def get_description(self):
        return self.description

    def take_damage(self,dmg):
        print(self.name, " took ", dmg, " of damage")
        self.hp -= dmg
        if self.hp <= 0:
            print(self.name, " is dead")
'''
Create all npcs here.
'''
thug_d = {"name": "Thug",
"description": "DESC_THUG",
"hp": 1500,
"attack": 75,
"hostile": True,
"inventory": [],
"boss":False
}

mutated_dog_d = {"name": "Mutated dog",
"description": "DESC_DOG",
"hp": 1000,
"attack": 120,
"hostile": True,
"inventory": [],
"boss":False
}

rogue_soldier_d = {"name": "Rogue soldier",
"description": "DESC_ROGUE",
"hp": 2000,
"attack": 175,
"hostile": True,
"inventory": [],
"boss":False
}

scavenger_d = {"name": "Scavenger",
"description": "DESC_SCAV",
"hp": 20000,
"attack": 150,
"hostile": True,
"inventory": [],
"boss":False
}

survivalist_d = {"name": "Survivalist",
"description": "DESC_SURV",
"hp": 2200,
"attack": 180,
"hostile": True,
"inventory": [],
"boss":False
}

'''
Those 4 below are the bosses. Only spawn in certain circustances
'''

coronel_d = {"name": "The coronel",
"description": "DESC_CORO",
"hp": 4000,
"attack": 200,
"hostile": True,
"inventory": [],
"boss":True
}

gravestone_d = {"name": "Gravestone",
"description": "DESC_GRAV",
"hp": 3800,
"attack": 2200,
"hostile": True,
"inventory": [],
"boss":True
}

sold13r_d = {"name": "SOLD13R",
"description": "DESC_SOLD",
"hp": 5000,
"attack": 250,
"hostile": True,
"inventory": [],
"boss":True
}

abomination_d = {"name": "Human abomination",
"description": "DESC_ABO",
"hp": 6000,
"attack": 220,
"hostile": True,
"inventory": [],
"boss":True
}

'''bosses = [coronel,gravestone,sold13r,abomination]'''


def spawn_npc():
    enemy_odd = random.randint(1,100)
    if enemy_odd < 20:
        thug = NPC(thug_d["name"],thug_d["description"],thug_d["hp"],thug_d["attack"],thug_d["hostile"],thug_d["inventory"],thug_d["boss"])
        return thug
    if enemy_odd >=20 and enemy_odd <= 39:
        mutated_dog = NPC(mutated_dog_d["name"],mutated_dog_d["description"],mutated_dog_d["hp"],mutated_dog_d["attack"],mutated_dog_d["hostile"],mutated_dog_d["inventory"],mutated_dog_d["boss"])
        return mutated_dog
    if enemy_odd >=40 and enemy_odd <=59:
        rogue_soldier = NPC(rogue_soldier_d["name"],rogue_soldier_d["description"],rogue_soldier_d["hp"],rogue_soldier_d["attack"],rogue_soldier_d["hostile"],rogue_soldier_d["inventory"],rogue_soldier_d["boss"])
        return rogue_soldier
    if enemy_odd >=60 and enemy_odd <=79:
        scavenger = NPC(scavenger_d["name"],scavenger_d["description"],scavenger_d["hp"],scavenger_d["attack"],scavenger_d["hostile"],scavenger_d["inventory"],scavenger_d["boss"])
        return scavenger
    if enemy_odd >=80 and enemy_odd <=99:
        survivalist = NPC(survivalist_d["name"],survivalist_d["description"],survivalist_d["hp"],survivalist_d["attack"],survivalist_d["hostile"],survivalist_d["inventory"],survivalist_d["boss"])
        return survivalist
    #BOSS
    if enemy_odd > 99:
        boss = spawn_boss()
        print("Get ready for the boss:")
        return boss

def spawn_boss():
    boss_index = random.randint(1,4)
    if boss_index == 1:
        coronel = NPC(coronel_d["name"],coronel_d["description"],coronel_d["hp"],coronel_d["attack"],coronel_d["hostile"],coronel_d["inventory"],coronel_d["boss"])
        return coronel
    if boss_index == 2:
        gravestone = NPC(gravestone_d["name"],gravestone_d["description"],gravestone_d["hp"],gravestone_d["attack"],gravestone_d["hostile"],gravestone_d["inventory"],gravestone_d["boss"])
        return gravestone
    if boss_index == 3:
        sold13r = NPC(sold13r_d["name"],sold13r_d["description"],sold13r_d["hp"],sold13r_d["attack"],sold13r_d["hostile"],sold13r_d["inventory"],sold13r_d["boss"])
        return sold13r
    if boss_index == 4:
        abomination = NPC(abomination_d["name"],sold13r_d["description"],sold13r_d["hp"],sold13r_d["attack"],sold13r_d["hostile"],sold13r_d["inventory"],sold13r_d["boss"])
        return abomination


    