from Common import *

class Enemy:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        #HP
        self.hp = 3
        # 座標(double, double)
        self.x = random.uniform(1, 3811)
        self.y = random.uniform(1, 2371)
        # 移動速度
        self.r = random.uniform(0.1, 1)
        # 弾用のタイマー
        self.time = pygame.time.get_ticks()
        # 角度
        self.rad = 1

    def update(self, player, enemy_bullet_manager):
        if player.x > self.x:
            self.x += self.r
        if player.y > self.y:
            self.y += self.r
        if player.x < self.x:
            self.x -= self.r
        if player.y < self.y:
            self.y -= self.r
        #弾発射
        if pygame.time.get_ticks() - self.time > 1000:
            self.time = pygame.time.get_ticks()
            x = 1.0
            y = 1.0
            r = 1.0
            rad = math.atan2((player.y-self.y),(player.x-self.x))
            enemy_bullet_manager.add(self.x, self.y, r, rad)

    # def valid(self, player):

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

        pygame.draw.circle(screen, (0,100,0),\
         (int(1100+self.x/15), int(50+self.y/15)), 3)
        pygame.draw.circle(screen, (0,255,0), (int(x), int(y)), 20)
        text = self.font.render(str(self.hp) , True, (0,0,0))
        screen.blit(text, (x, y))

    def valid(self, player_bullet_manager):
        #敵と自機の衝突判定
        for bullet in player_bullet_manager.bullets:
            if bullet.x -19 <= self.x <= bullet.x +19 and \
               bullet.y -19 <= self.y <= bullet.y +19:
                player_bullet_manager.bullets.remove(bullet)
                self.hp -= 1
        return self.hp < 1

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
