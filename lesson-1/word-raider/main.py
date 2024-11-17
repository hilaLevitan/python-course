from game import Game
words_list = []
with open("words.txt", "r") as words_file:
    words_list.extend(words_file.read().splitlines())

game = Game(words_list)
game_on = True
while game_on:
    game.play()
    result = input("Do you want to keep playing? (y/n)")
    if result.lower() != "y":
        game_on = False
    game.reset()

print("Game is over")