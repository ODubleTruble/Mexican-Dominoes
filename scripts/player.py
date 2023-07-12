class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_tile_to_hand(self, tile):
        self.hand.append(tile)
    
    def remove_tile_from_hand(self, tile):
        self.hand.remove(tile)

    def print_hand(self):
        print(f"{self.name}'s hand:")
        for tile in self.hand:
            print(tile)
        