from Common import *

class Bullet:
    def __int__(self):
        self.x = 0
        self.y = 0
        self.r = 0
        self.rad = 0

    def update(self, screen):
        self.x += self.r
        self.y += self.r

    def draw(self):
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 20)
