class Tile:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return f"[{self.side1}|{self.side2}]"
    
    def __eq__(self, other):
        return (self.side1 == other.side1 and self.side2 == other.side2) or \
               (self.side1 == other.side2 and self.side2 == other.side1)
