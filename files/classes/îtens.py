class itens():
    def __init__(self,name,quantity,description):
        self.name = name
        self.quantity = quantity
        self.description = description

        def get_name():
            return self.name
        
        def get_quantity():
            return self.quantity

        def get_description():
            return self.description

        def use_item():
            if self.quantity <= 0:
                print("You dont have " + self.name +" to use")
            else:
                #do something...
                self.quantity -= 1