from scripts.tile import Tile
from scripts.dominoset import DominoSet
from scripts.player import Player


min_dots = 1
max_dots = 6
starting_dominoes = 3
total_players = 2
shuffle = True


# Create the domino set.
dominoes = DominoSet()
dominoes.generate_set(min_dots, max_dots)
if shuffle: dominoes.shuffle()
dominoes.print_all_tiles()


# Create players and deal starting dominoes
players = []
for i in range(total_players):
    players.append(Player(f'Player {i+1}'))
for player in players:
    for i in range(starting_dominoes):
        new_tile = dominoes.deal_new_tile()
        player.add_tile_to_hand(new_tile)

for player in players:
    player.print_hand()
dominoes.print_all_tiles()


# Implement game logic
# ...
