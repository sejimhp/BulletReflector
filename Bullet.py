from Common import *

class Bullet:
    def __init__(self, x, y, r, rad):
        self.x = x
        self.y = y
        self.r = r
        self.rad = rad
        self.image = 0

    def valid(self, stage):
        if self.x < 0 or self.y < 0:
            return False
        elif self.x > stage.img_rect[2] or self.y > stage.img_rect[3]:
            return False
        return True

    def update(self):
        x = self.r * math.cos(self.rad)
        y = self.r * math.sin(self.rad)
        self.x += x
        self.y += y

    def draw(self, screen, player, stage):
        x = self.x
        y = self.y
        if player.x > SCREEN_SIZE[0]/2:
            x -= (player.x - SCREEN_SIZE[0]/2)
        if player.y > SCREEN_SIZE[1]/2:
            y -= (player.y - SCREEN_SIZE[1]/2)
        if player.x + SCREEN_SIZE[0]/2 > stage.img_rect[2]:
            x = self.x - (stage.img_rect[2] - SCREEN_SIZE[0])
        if player.y + SCREEN_SIZE[1]/2 > stage.img_rect[3]:
            y = self.y - (stage.img_rect[3] - SCREEN_SIZE[1])

        screen.blit(self.image, (int(x), int(y)))

class MyBullet(Bullet):
    def __init__(self, x, y, r, rad):
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/player_bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

class EnemyBullet(Bullet):
    def __init__(self, x, y, r, rad):
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/enemy1_bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

class Arrow(Bullet):
    def __init__(self, x, y, r, rad):
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/arrow.png")


class Laser(Bullet):
    def __init__(self, x, y, r, rad):
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/laser.png")
