import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
	def __init__(self):

		self.display_surface = pygame.display.get_surface()

		self.visible_sprites = CameraGroup()
		self.active_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()

		self.setup_level()

	def setup_level(self):
			for row_index,row in enumerate(LEVEL_MAP):
				for col_index,col in enumerate(row):
					x = col_index * TILE_SIZE
					y = row_index * TILE_SIZE
					if col == 'X':
						Tile((x,y),[self.visible_sprites,self.collision_sprites])
					elif col == 'P':
						self.player = Player((x,y),[self.visible_sprites,self.active_sprites],self.collision_sprites)
						self.player_starting_pos = (x,y)
					




					

	def run(self):
		self.active_sprites.update()
		self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2(100,300)

	
		cam_left = CAMERA_BORDERS['left']
		cam_top = CAMERA_BORDERS['top']
		cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS['right'])
		cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS['bottom'])

		self.camera_rect = pygame.Rect(cam_left,cam_top,cam_width,cam_height)

	def custom_draw(self,player):

		if player.rect.left < self.camera_rect.left:
			self.camera_rect.left = player.rect.left
		if player.rect.right > self.camera_rect.right:
			self.camera_rect.right = player.rect.right
		if player.rect.top < self.camera_rect.top:
			self.camera_rect.top = player.rect.top
		if player.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = player.rect.bottom

		self.offset = pygame.math.Vector2(
			self.camera_rect.left - CAMERA_BORDERS['left'],
			self.camera_rect.top - CAMERA_BORDERS['top'])

		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
