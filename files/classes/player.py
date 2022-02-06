class Player():
    def __init__(self,name,level,max_hp,current_hp,skill_points,inventory, money):
        self.name = name
        self.level = level
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.skill_points = skill_points
        self.inventory = inventory
        self.money = money

    #Getters
    def get_name(self): 
        return self.name

    def get_level(self):
        return self.level
    
    def get_max_hp(self):
        return self.max_hp

    def get_current_hp(self):
        return self.current_hp

    def get_skill_points(self):
        return self.skill_points

    def get_inventory(self):
        return self.inventory

    def get_money(self):
        return self.money

    def set_nome(self,name):
        self.name = name

    #Now we start the good stuff
    def take_damage(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            print(self.nome + " morreu.")
            print("GAME OVER")
        return self.hp