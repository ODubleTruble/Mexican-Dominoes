import random
from scripts.tile import Tile


class DominoSet:
    def __init__(self):
        self.tiles = []

    def generate_set(self, min_dots, max_dots):
        # min_dots and max_dots are the minimum and maximum values that each side of a tile can be.
        
        for side1 in range(min_dots, max_dots+1):
            for side2 in range(min_dots, max_dots+1):
                new_tile = Tile(side1, side2)
                self.add_tile(new_tile)
            min_dots += 1
    
    def add_tile(self, tile):
        self.tiles.append(tile)
    
    def remove_tile(self, tile):
        self.tiles.remove(tile)
    
    def shuffle(self):
        random.shuffle(self.tiles)

    def get_all_tiles(self):
        return self.tiles

    def print_all_tiles(self):
        print(f'{len(self.tiles)} dominoes in set:')
        for tile in self.tiles:
            print(tile)

    def deal_new_tile(self):
        new_tile = self.tiles.pop()
        return new_tile
