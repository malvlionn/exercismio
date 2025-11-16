# Globals for the directions
# Change the values as you see fit
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"
listarah = [EAST, SOUTH, WEST, NORTH]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, arahbaru):
        x_pos, y_pos = self.coordinates
        
        for gerakan in arahbaru:
            if gerakan == "R":
                self.direction = listarah[(listarah.index(self.direction) + 1) % 4]
            elif gerakan == "L":
                self.direction = listarah[(listarah.index(self.direction) - 1) % 4]
            elif gerakan == "A":
                if self.direction == NORTH:
                    y_pos += 1
                elif self.direction == SOUTH:
                    y_pos -= 1
                elif self.direction == EAST:
                    x_pos += 1
                elif self.direction == WEST:
                    x_pos -= 1
        self.coordinates = (x_pos, y_pos)