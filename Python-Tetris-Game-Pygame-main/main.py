import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
pest_surface = title_font.render("Pest Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Press Space", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
pest_rect = pygame.Rect(320, 550, 170, 60)
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()
game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)
x=game.pest_score

while True:
    
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
			if event.key == pygame.K_SPACE and game.game_over == True:
				game.game_over=False
				game.reset()
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	
	score_value_surface = title_font.render(str(game.score), True, Colors.white)
 
	score_pest_surface = title_font.render(str(x), True, Colors.green)
	
 
	bg=pygame.image.load("Python-Tetris-Game-Pygame-main/assets/pgTH1.png")
	screen.blit(bg,(0,0))
 
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))
	screen.blit(pest_surface, (330, 500, 50, 50))


	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
 
	pygame.draw.rect(screen, Colors.light_blue,pest_rect, 0, 10)
	screen.blit(score_pest_surface, score_pest_surface.get_rect(centerx = pest_rect.centerx, 
		centery = pest_rect.centery))
 
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60)