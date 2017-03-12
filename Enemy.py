from Common import *

enemy1 = pygame.image.load("image/enemy1.png")
enemy2 = pygame.image.load("image/enemy2.png")
enemy3 = pygame.image.load("image/enemy3.png")
enemy4 = pygame.image.load("image/enemy4.png")

class Enemy:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        # 座標(double, double)
        self.x = random.uniform(1, 3811)
        self.y = random.uniform(1, 2371)
        # 弾用のタイマー
        self.time = pygame.time.get_ticks()
        # 角度
        self.rad = 2
        # 機ID
        self.id = 0

    def update(self, player, enemy_bullet_manager):
        if player.x > self.x:
            self.x += self.r
        if player.y > self.y:
            self.y += self.r
        if player.x < self.x:
            self.x -= self.r
        if player.y < self.y:
            self.y -= self.r

    def valid(self, player_bullet_manager):
        #弾と敵機の当たり判定
        for bullet in player_bullet_manager.bullets:
           if bullet.id == 1:#普通の弾
               if bullet.x -30 <= self.x <= bullet.x +40 and \
                bullet.y -35 <= self.y <= bullet.y +35:
                   player_bullet_manager.bullets.remove(bullet)
                   self.hp -= 1
           elif bullet.id == 3: # 矢
               if bullet.x -20 <= self.x <= bullet.x + 50 and \
                bullet.y -20 <= self.y <= bullet.y + 50:
                   player_bullet_manager.bullets.remove(bullet)
                   self.hp -= 1
           elif bullet.id == 5:
               if bullet.x -60 <= self.x <= bullet.x + 60 and \
                bullet.y -60 <= self.y <= bullet.y + 60:
                   self.hp -= 100

        return self.hp < 1

    def rotate_blit(dst_surf, src_surf, pos, angle, center=True):
        #回転させたイメージの作成
        rotateimg = pygame.transform.rotate(src_surf,angle)

        w1, h1 = src_surf.get_size()  #回転前のサイズ
        w2, h2 = rotateimg.get_size() #回転後のサイズ

        if center:
            topleft = (pos[0] - w2 / 2, pos[1] - h2 / 2)
        else:
            dx, dy = (w2 - w1) / 2, (h2 - h1) / 2
            topleft = (pos[0] - dx, pos[1] - dy)
        dst_surf.blit(rotateimg, topleft)
        return rotateimg, topleft

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

        self.rad += 1
        image, (x, y) = rotate_blit(screen, self.image, (x, y), self.rad, True)

        pygame.draw.circle(screen, (0,100,0),\
         (int(1100+self.x/15), int(50+self.y/15)), 3)
        screen.blit(image, (int(x), int(y)))
        # text = self.font.render(str(self.x) + " , " + str(self.y) , True, (255,255,255))
        # screen.blit(text, (x, y))

class Enemy1(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        # ID
        self.id = 1
        #HP
        self.hp = 5
        # 移動速度
        self.r = random.uniform(0.1, 1)
        self.image = enemy1
    def update(self, player, enemy_bullet_manager):
        Enemy.update(self, player, enemy_bullet_manager)
        #弾発射
        if pygame.time.get_ticks() - self.time > 1000:
            self.time = pygame.time.get_ticks()
            x = 1.0
            y = 1.0
            r = 1.0
            rad = math.atan2((player.y-self.y),(player.x-self.x))
            enemy_bullet_manager.add(self.x, self.y, r, rad, 2)

class Enemy2(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        # ID
        self.id = 2
        #HP
        self.hp = 3
        # 移動速度
        self.r = 0
        self.image = enemy2
    def update(self, player, enemy_bullet_manager):
        Enemy.update(self, player, enemy_bullet_manager)
        #弾発射
        if pygame.time.get_ticks() - self.time > 5000:
            self.time = pygame.time.get_ticks()
            x = 2.0
            y = 2.0
            r = 1.0
            rad = math.atan2((player.y-self.y),(player.x-self.x))
            enemy_bullet_manager.add(self.x, self.y, r, rad, 3)

class Enemy3(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        # ID
        self.id = 3
        #HP
        self.hp = 1
        # 移動速度
        self.r = random.uniform(1.5, 2.5)
        self.image = enemy3

class Enemy4(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        # ID
        self.id = 4
        #HP
        self.hp = 2
        self.interval = pygame.time.get_ticks()
        # 移動速度
        self.r = random.uniform(0.1, 1)
        self.image = enemy4
    def update(self, player, enemy_bullet_manager):
        Enemy.update(self, player, enemy_bullet_manager)
        #弾発射
        if pygame.time.get_ticks() - self.time < 5000:
            if pygame.time.get_ticks() - self.interval > 5000 / 20:
                self.interval = pygame.time.get_ticks()
                x = 4.0
                y = 4.0
                r = 1.0
                rad = math.atan2((player.y-self.y),(player.x-self.x))
                enemy_bullet_manager.add(self.x, self.y, r, rad, 4)
        elif pygame.time.get_ticks() - self.time > 10000:
            self.time = pygame.time.get_ticks()
