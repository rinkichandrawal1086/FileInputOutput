# games=[ "Chess","Ludo","cards","football","Cricket", "Badminton","Tennis"]
# with open("test.txt",'w') as games_file:
#     for game in games:
#         print(game, file=games_file)

games=[]
with open("games.txt",'r') as game_file:
    for game in game_file:
        games.append(game.strip("\n"))

print(games)
for game in games:
    print(game)

