import pygame

import os
print(os.getcwd()) #Esto sirve para ver en que directorios cree python que está guardado el programa


class Ship():
	'''Initialize the sip and set it´s starting position'''
	def __init__(self, ai_settings, screen):	
		'''Initialize the sip and set it´s starting position'''
		self.screen = screen
		self.ai_settings = ai_settings

		#Load the ship image and get it`s rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		#Start each new spaceship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Allow floats in the ship´s speed factor
		self.center = float(self.rect.centerx)
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):#Moves the ship when flag is changed 
		if self.moving_right and self.rect.centerx < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		
		elif self.moving_left and self.rect.centerx > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		#Adjust the self.rect.centerx movement(which is the ship) to
		#self.center movement
		self.rect.centerx = self.center
	
	def center_ship(self):
		'''Put the ship in the center of the screen'''
		self.center = self.screen_rect.centerx 
		
	def blitme(self):
		'''Draw the ship at its current location'''
		self.screen.blit(self.image, self.rect)
