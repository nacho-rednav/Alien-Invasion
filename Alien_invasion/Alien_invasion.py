import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#Initialize and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
		ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	#Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	scoreboard = Scoreboard(ai_settings, screen, stats)
	#Instance of Button to play
	play_button = Button(ai_settings, screen, "PLAY")

	#Make a ship, group of aliens and group of bullets	
	ship = Ship(ai_settings, screen)
	aliens = pygame.sprite.Group()
	bullets = pygame.sprite.Group()
	superbullets = pygame.sprite.Group()

	
	#Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, aliens, ship)
	
	
	#Start the main loop for the game
	while True:
		
		#Watch for keyboards and mouse events
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, superbullets, scoreboard)
		if stats.game_active:
		#These functions only have to run when game is active
			#Update ship's position
			ship.update()
			#Updates bullets' and aliens' positions
			gf.update_bullets(ai_settings, screen, stats, scoreboard,ship, aliens, bullets, superbullets)
			gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard)
			#Create new fleet when the previous one is destroyes
			gf.repopulate_fleet(ai_settings, screen, aliens, ship, superbullets, bullets, stats, scoreboard)				
		#Update images and flip to the new screen
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, superbullets, play_button, scoreboard)
		
		
	
run_game()
