"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """kocak"""
    total_aliens_created = 0
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1
    def hit(self):
        self.health -= 1
    def is_alive(self):
        return self.health > 0
    def teleport(self, xcoor, ycoor):
        self.x_coordinate = xcoor
        self.y_coordinate = ycoor
    def collision_detection(self, object):
        pass
        
def new_aliens_collection(posisi):
    return [Alien(koorx,koory) for koorx,koory in posisi]