import game as Game


'''
This class will run an instance of game.py
Ideally, this file should contain only callout to the game.py methods
'''

is_game_running = True
number_of_rooms = 0

#Create an instance of the game class
game_instance = Game.game
#Start the game
game_instance.start_game()


while is_game_running:
    game_instance.choose_room()
    if Game.player_choose_room == True:
        game_instance.generate_enemies()
        keep_game = game_instance.check_if_player_is_alive()
        if keep_game == True:
            is_game_running = True
            number_of_rooms +=1
        else:
            is_game_running = False
    else:
        print("\n")

print("\n\nGAME OVER\n\n")
print("You survived ",number_of_rooms, " rooms")