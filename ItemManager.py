from Common import *

class ItemManager:
	def __init__(self):
		self.time = pygame.time.get_ticks()
		self.items = []

	def update(self, player):
		if self.time > 100:
			self.time = pygame.time.get_ticks()
			self.items.append(Item())
		# 接触判定
		for item in self.items:
			item.update(player)

	def draw(self, screen, player, stage):
		for item in self.items:
			item.draw(screen, player, stage)
