from Common import *

class ItemManager:
	def __init__(self):
		self.time = pygame.time.get_ticks()
		self.items = []

	def update(self, player)
		if pygame.time.get_ticks() -self.time > 5000:
			self.time = pygame,time.get_ticks()
			self.items.append(Item())

		for item in self.items:
			item.update(player)

	def draw(self, screen, player, stage):
		for item in self.items:
			item.draw(screen, player, stage)
