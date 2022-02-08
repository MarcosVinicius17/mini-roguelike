class Player():
    def __init__(self,name,max_hp,current_hp,first_aid_kits):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.first_aid_kits = first_aid_kits

    #Getters
    def get_name(self): 
        return self.name
    
    def get_max_hp(self):
        return self.max_hp

    def set_hp(self, heal):
        self.current_hp += heal

    def get_current_hp(self):
        return self.current_hp

    def get_first_aid_kits(self):
        return self.first_aid_kits

    def use_first_aid_kits(self):
        self.first_aid_kits -= 1

    def win_first_aid_kit(self):
        self.first_aid_kits +=1

    def set_nome(self,name):
        self.name = name

    #Now we start the good stuff
    def take_damage(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            print(self.nome + " morreu.")
            print("GAME OVER")
        return self.hp

    def attack(enemy,damage):
        enemy.take_damage(damage)

    def heal(self):
        current_faks = Player.get_first_aid_kits(self)
        if current_faks >= 1:
            print("Healing")
            Player.set_hp(self,100)
            Player.use_first_aid_kits(self)
        else:
            print("You have zero first aid kits.\n") 