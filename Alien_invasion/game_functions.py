import sys
from time import sleep
import pygame
from bullets import Bullets, Superbullets
from alien import Alien

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, superbullets, scoreboard):
	#Watch for keyboards and mouse events
		for event in pygame.event.get():			
			#Ship's movement, firing bullets and exit
			if event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets, superbullets)										
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)	
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_buttons(ai_settings, screen, stats, ship, aliens, 
					bullets, superbullets, play_button, mouse_x, mouse_y, scoreboard)
def check_play_buttons(ai_settings, screen, stats, ship, aliens, bullets, 
		superbullets, play_button, mouse_x, mouse_y, scoreboard):
	'''Start new game when the player clicks Play'''
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#Reset game settings
		ai_settings.initialize_dynamic_settings()

		stats.reset_stats()
		stats.game_active = True
		#Reset scoreboard
		scoreboard.prep_score()
		scoreboard.prep_level()
		scoreboard.prep_ships()
		#Hide mouse cursor
		pygame.mouse.set_visible(False)

		#Empty the list of aliens, bullets and superbullets
		aliens.empty()
		bullets.empty()
		superbullets.empty()

		#Create new fleet and center the ship
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()			
def check_keydown_events(event, ai_settings, screen, ship, bullets, superbullets):
	#Quitting the game
	if event.key == pygame.K_q:
		sys.exit()
	
	elif event.key == pygame.K_RIGHT:
		#Move the ship to the right
		ship.moving_right = True
				
	elif event.key == pygame.K_LEFT:
		#Move the ship to the left
		ship.moving_left = True	
	
	elif event.key == pygame.K_SPACE:
		#Create a new bullet and add it to the bullets group
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullets(ai_settings, screen, ship)
			bullets.add(new_bullet)	

	elif event.key == pygame.K_TAB:
		#Create a superbullet an add it to superbullets group
		if len(superbullets) < ai_settings.superbullets_allowed:
			new_superbullet = Superbullets(ai_settings, screen, ship)
			superbullets.add(new_superbullet)		
def check_keyup_events(event, ship):					
	#Allow keepping the KEY pressed to move
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
				
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False				


#All this functions are used to create the fleet
def get_number_rows(ai_settings, alien_height, ship_height):
	'''Determine the number of rows that fit in the screen'''
	#Distance between rows = alien´s height. 2 alien´s height away from the ship
	available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
	number_rows = int(available_space_y / (2* alien_height))
	return number_rows
def get_number_aliens(ai_settings, alien_width):
	'''Calculate the number of aliens that fit in a row'''
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int((available_space_x / (2 * alien_width))-1)#-1 para tener un espacio a la derecha de la pantalla
	return  number_aliens_x
def create_alien(ai_settings, screen, aliens, alien_number, row_number):	
		'''Create an alien and place it in the row'''
		alien = Alien(ai_settings, screen)
		alien_width = alien.rect.width
		alien.rect.x =  alien_width  + 2*alien_width * alien_number
		alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
		aliens.add(alien)
def create_fleet(ai_settings, screen, aliens, ship):
	'''Create a full fleet of aliens'''
	# Create an alien and find the number of aliens in a row
	# Spacing between aliens is equal to one alien´s width
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
	number_rows = get_number_rows(
		ai_settings, alien.rect.height, ship.rect.height)
	#Create rows of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(
			ai_settings, screen, aliens, alien_number, row_number)	


def check_fleet_edges(ai_settings, aliens):
	'''Respond correctly if any alien reaches an edge'''
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard):
	'''Respond to alien-ship collision
	Change flag if all ships are destroyed'''
	if stats.ships_left > 0:
		#Decrement ships left
		stats.ships_left -= 1

		#Empty the list of aliens, bullets and superbullets
		aliens.empty()
		bullets.empty()
		superbullets.empty()

		#Create a new ship and center the ship
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()

		#Update scoreboard
		scoreboard.prep_ships()

		#Pause
		sleep(1.0)
	else:
		stats.game_active = False
		#Shoe mouse cursor
		pygame.mouse.set_visible(True)
def check_aliens_bottom(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard):
	'''Check if any alien hits the bottom of the screen'''
	screen_rect = screen.get_rect()
	for alien in aliens:
		if alien.rect.bottom >= screen_rect.bottom:
			#Same as if ship-alien collide
			ship_hit(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard)
def update_aliens(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard):
	'''Move the entire fleet'''
	check_fleet_edges(ai_settings, aliens)
	aliens.update(aliens)
	#Check for aliens hitting the bottom
	check_aliens_bottom(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard)
	#Check collisions between the ship and the aliens
	if pygame.sprite.spritecollideany(ship, aliens):
		print("SHIP HIT!!")
		ship_hit(ai_settings, stats, screen, aliens, ship, bullets, superbullets, scoreboard)


def check_bullet_alien_collisions(ai_settings, screen, stats, scoreboard, ship, aliens,
	 bullets, superbullets):
	'''Checks if user hits aliens and adds score points'''	
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	supcollisions = pygame.sprite.groupcollide(superbullets, aliens, False, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			scoreboard.prep_score()
	if supcollisions:	
		for aliens in supcollisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			scoreboard.prep_score()
def update_bullets(ai_settings, screen, stats, scoreboard,ship, aliens, bullets, superbullets):
	'''Changes bullets and superbullets position an deletes bullets'''
	bullets.update()
	superbullets.update()
	#Don´t delete superbullets, limited number of them per game
	for bullet in bullets:
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	#Check if a bullet hits an alien
	check_bullet_alien_collisions(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, superbullets)


def repopulate_fleet(ai_settings, screen, aliens, ship, superbullets, bullets, stats, scoreboard):
	'''Create new fleet, destroy bullets and speed up game after when all aliens are dead'''
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, aliens, ship)
		superbullets.empty() #To allow shooting superbullets again
		#Level up
		stats.level += 1
		scoreboard.prep_level()

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, superbullets, play_button, scoreboard):
	'''Update images and flip to the new screen'''
	#Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	#Redraw all bullets and superbullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	for superbullet in superbullets.sprites():
		superbullet.draw_superbullet()

	#Draw the ship	 
	ship.blitme()
	#Draw the aliens
	aliens.draw(screen)
	#Draw scoreboard
	scoreboard.show_score()

	#If game is inactive draw the play button
	if not stats.game_active:
		play_button.draw_button()
				
	#Make the most recently drawn screen visible
	pygame.display.flip()
