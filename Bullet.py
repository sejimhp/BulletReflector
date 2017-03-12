from Common import *

class Bullet:
    def __init__(self, x, y, r, rad):
        self.font = pygame.font.Font(None, 30)
        self.x = x
        self.y = y
        self.r = r
        self.rad = rad
        self.image = 0
        self.id

    def valid(self, stage):
        if self.x < 0 or self.y < 0:
            return False
        elif self.x > stage.img_rect[2] or self.y > stage.img_rect[3]:
            return False
        return True

    def update(self, player):
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
        self.id = 1
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/player_bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

class EnemyBullet(Bullet):
    def __init__(self, x, y, r, rad):
        self.id = 2
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/enemy1_bullet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

class Arrow(Bullet):
    def __init__(self, x, y, r, rad):
        self.id = 3
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/arrow.png")
        # 矢印の向き
        if abs(rad) < (math.pi/2): # 右半分の処理
            self.image = pygame.transform.flip(self.image ,True, False)
            self.image = pygame.transform.rotate(self.image, -(math.pi/2+rad)*180/math.pi)
        else: # 左半分の処理
            self.image = pygame.transform.flip(self.image ,True ,True)
            self.image = pygame.transform.rotate(self.image, (math.pi/2 - rad)*180/math.pi)
    def update(self, player):
        Bullet.update(self, player)
        if self.r == 0:
            self.x = player.x - 20
            self.y = player.y - 20
            self.pressed_keys = pygame.key.get_pressed()
            if self.pressed_keys[K_SPACE]:
                self.r = 8

class EnemyLaser(Bullet):
    def __init__(self, x, y, r, rad):
        self.id = 4
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/enemy_laser.png")

class PlayerLaser(Bullet):
    def __init__(self, x, y, r, rad):
        self.id = 5
        Bullet.__init__(self, x, y, r, rad)
        self.image = pygame.image.load("image/player_laser.png")
        # レーザーの向き
        if abs(rad) < (math.pi/2): # 右半分の処理
            self.image = pygame.transform.flip(self.image ,True, False)
            self.image = pygame.transform.rotate(self.image, -(math.pi/2+rad)*180/math.pi)
        else: # 左半分の処理
            self.image = pygame.transform.flip(self.image ,True ,True)
            self.image = pygame.transform.rotate(self.image, (math.pi/2 - rad)*180/math.pi)
