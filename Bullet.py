from Common import *

class Bullet:
    def __int__(self, x, y, r, rad):
        self.x = x
        self.y = y
        self.r = r
        self.rad = rad

    def update(self, screen):
        self.x += self.r
        self.y += self.r

    def draw(self):
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
