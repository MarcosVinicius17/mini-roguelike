import random

class Weapon():
    def __init__(self,name, damage, crit_chance,isRanged):
        self.name = name
        self.damage = damage
        self.crit_chance = crit_chance
        self.isRanged = isRanged

        def get_name(self):
            return self.name
        
        def get_damage(self):
            return self.damage
        
        def get_crit_chance(self):
            return self.crit_chance

        def get_isRanged(self):
            return self.isRanged

        def is_a_crit(self):
        #generates a random number between 1 and 100. If is less or equal than the crit chance, the next attack will be a critical hit
           chance = random.randint(1,100)
           if chance <= self.crit_chance:
               print("CRITICAL HIT")
               return True
           return False
         
        def use_weapon(self):
            if self.isRanged == True:
                #there is ammunition available??
                print("do something...")
            
            
            