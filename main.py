import pygame, sys

import colors
from game import Game
from colors import Colors
from grid import Grid



pygame.init() #initialize pygame

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)
bom_surface = title_font.render("Boms", True, Colors.white)
image_surface = pygame.image.load("Image/bomimage2.png")

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
bom_rect = pygame.Rect(320, 450, 170, 70)

screen = pygame.display.set_mode((500,620)) # width and height
pygame.display.set_caption("Tetris by Pygame")

clock = pygame.time.Clock() #FPS control

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

gameLoop = True

bom_trigger = 0

while gameLoop:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameLoop = False
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			bom_trigger = 20
			game.bom(int(y/30), int(x/30))
			# print(int(y / 30), int(x / 30))

		if event.type == pygame.KEYDOWN:
			if game.game_over:
				game.game_over = False
				game.reset()
			if event.key == pygame.K_LEFT and not game.game_over:
				game.move_left()
			if event.key == pygame.K_RIGHT and not game.game_over:
				game.move_right()
			if event.key == pygame.K_DOWN and not game.game_over:
				game.move_down()
				game.update_score(0,1)
			if event.key == pygame.K_UP and not game.game_over:
				game.rotate()
			if event.key == pygame.K_p:
				Grid.print_grid(game.grid)

		if event.type == GAME_UPDATE and not game.game_over:
			game.move_down()


	#Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.white)
	bom_value_surface = title_font.render(str(game.boms), True, Colors.white)
	screen.fill(Colors.dark_blue)
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))
	screen.blit(bom_surface, (365, 420, 50, 50))
	# screen.blit(image_surface, (100, 100, 50, 50))

	if bom_trigger and game.boms and int(y/30)<20 and int(x/30)<10:
		screen.blit(image_surface, (x - 30, y - 30))
		bom_trigger -= 1

	if game.game_over:
		screen.blit(game_over_surface, (320, 550, 50, 50))

	pygame.draw.rect(screen, Colors.light_blue, score_rect,0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))

	pygame.draw.rect(screen,Colors.light_blue, bom_rect, 0, 10)
	screen.blit(bom_value_surface, bom_value_surface.get_rect(centerx = bom_rect.centerx, centery = bom_rect.centery))

	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60)