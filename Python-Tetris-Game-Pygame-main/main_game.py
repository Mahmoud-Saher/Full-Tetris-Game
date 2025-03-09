import pygame, sys
from button import Button
from game import Game
from colors import Colors


pygame.init()
game = Game()
SCREEN = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Python-Tetris-Game-Pygame-main/assets/pack.jpg")
pygame.mixer.init()
pygame.mixer.music.load(f"Python-Tetris-Game-Pygame-main/Sounds/music2.ogg")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)


def get_font(size): 
    return pygame.font.Font("Python-Tetris-Game-Pygame-main/assets/font.ttf", size)

def play():
    pygame.init()
    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.white)
    next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("Press Space", True, Colors.white)
    score_rect = pygame.Rect(320, 55, 170, 60)
    pest_surface = title_font.render("Best Score", True, Colors.white)
    next_rect = pygame.Rect(320, 215, 170, 180)
    pest_rect = pygame.Rect(320, 550, 170, 60)
    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()
    
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

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

            #Drawing
            score_value_surface = title_font.render(str(game.score), True, Colors.white)
            score_pest_surface = title_font.render(str(game.pest_score), True, Colors.green)

            screen.fill(Colors.dark_blue)
            screen.blit(score_surface, (365, 20, 50, 50))
            screen.blit(next_surface, (375, 180, 50, 50))
            screen.blit(pest_surface, (330, 500, 50, 50))
            
            if game.game_over == True:
                over_menu()

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

def play_again():
    pygame.init()
    game=Game()
    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.white)
    next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("Press Space", True, Colors.white)
    score_rect = pygame.Rect(320, 55, 170, 60)
    pest_surface = title_font.render("Best Score", True, Colors.white)
    next_rect = pygame.Rect(320, 215, 170, 180)
    pest_rect = pygame.Rect(320, 550, 170, 60)
    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()
    
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

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

            #Drawing
            score_value_surface = title_font.render(str(game.score), True, Colors.white)
            score_pest_surface = title_font.render(str(game.pest_score), True, Colors.green)

            screen.fill(Colors.dark_blue)
            screen.blit(score_surface, (365, 20, 50, 50))
            screen.blit(next_surface, (375, 180, 50, 50))
            screen.blit(pest_surface, (330, 500, 50, 50))
            
            if game.game_over == True:
                over_menu()

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
            
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        MAIN_TEXT = get_font(40).render("OPTIONS", True, "White")
        MAIN_RECT = MAIN_TEXT.get_rect(center=(250, 25))
        SCREEN.blit(MAIN_TEXT, MAIN_RECT)

        OPTIONS_TEXT = get_font(30).render("Volume", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(250, 150))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(250, 500),text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")
        OPTIONS_Theems = Button(image=None, pos=(250, 350), 
                            text_input="Themes", font=get_font(25), base_color="White", hovering_color="Green")
        OPTIONS_INC = Button(image=None, pos=(350, 200),text_input=">", font=get_font(15), base_color="White", hovering_color="Green")
        OPTIONS_DEC = Button(image=None, pos=(150, 200),text_input="<", font=get_font(15), base_color="White", hovering_color="Green")
        OPTIONS_MUTE = Button(image=None, pos=(250, 200),text_input="Mute", font=get_font(15), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_Theems.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Theems.update(SCREEN)
        OPTIONS_INC.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_INC.update(SCREEN)
        OPTIONS_DEC.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_DEC.update(SCREEN)
        OPTIONS_MUTE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MUTE.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                i=0.5
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_INC.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.unpause()
                    i=i+0.2
                    pygame.mixer.music.set_volume(i)
                if OPTIONS_DEC.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.unpause()
                    i=i-0.2
                    pygame.mixer.music.set_volume(i)
                if OPTIONS_MUTE.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.pause()
                if OPTIONS_Theems.checkForInput(OPTIONS_MOUSE_POS):
                    Themes()
        pygame.display.update() 
def Themes():
    image1 = pygame.image.load("Python-Tetris-Game-Pygame-main/assets/TH1.png")

    def TH1(image1):       #Theem 1
        size = pygame.transform.scale(image1,(150, 150))
        SCREEN.blit(size,(30, 130))
            
    image2 = pygame.image.load("Python-Tetris-Game-Pygame-main/assets/TH2.png")

    def TH2(image2):       #Theem 2
        size = pygame.transform.scale(image2,(150, 150))
        SCREEN.blit(size,(320, 130))
        
    image3 = pygame.image.load("Python-Tetris-Game-Pygame-main/assets/TH3.png")

    def TH3(image3):       #Theem 3
        size = pygame.transform.scale(image3,(150,150))
        SCREEN.blit(size,(30, 380))
        
    image4 = pygame.image.load("Python-Tetris-Game-Pygame-main/assets/TH4.png")

    def TH4(image4):       #Theem 4
        size = pygame.transform.scale(image4,(150,150))
        SCREEN.blit(size,(320, 380))

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))
        
        OPTIONS_TEXT = get_font(25).render("Choose Your Theme: ", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(250, 25))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(250, 550), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        OPTIONS_Theem1 = Button(image=None, pos=(100, 100), 
                            text_input="Theme 1", font=get_font(15), base_color="White", hovering_color="Green")
        
        OPTIONS_Theem1.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Theem1.update(SCREEN)
        TH1(image1)

            

        OPTIONS_Theem2 = Button(image=None, pos=(400, 100), 
                            text_input="Theme 2", font=get_font(15), base_color="White", hovering_color="Green")
        
        OPTIONS_Theem2.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Theem2.update(SCREEN)
        TH2(image2)


        OPTIONS_Theem3 = Button(image=None, pos=(100, 350), 
                            text_input="Theme 3", font=get_font(15), base_color="White", hovering_color="Green")
        
        OPTIONS_Theem3.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Theem3.update(SCREEN)
        TH3(image3)

            
        OPTIONS_Theem4 = Button(image=None, pos=(400, 350), 
                            text_input="Theme 4", font=get_font(15), base_color="White", hovering_color="Green")
        
        OPTIONS_Theem4.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Theem4.update(SCREEN)
        TH4(image4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_Theem1.checkForInput(OPTIONS_MOUSE_POS):
                    play()
                if OPTIONS_Theem2.checkForInput(OPTIONS_MOUSE_POS):
                    Colors.them=2
                    play()
                if OPTIONS_Theem3.checkForInput(OPTIONS_MOUSE_POS):
                    play()
                if OPTIONS_Theem4.checkForInput(OPTIONS_MOUSE_POS):
                    play()           
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()        

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("TETRIS GAME", True, "YELLOW")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Python-Tetris-Game-Pygame-main/assets/Play Rect.png"), pos=(240, 200), 
                            text_input="PLAY", font=get_font(20), base_color="White", hovering_color="Red")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Python-Tetris-Game-Pygame-main/assets/Play Rect.png"), pos=(240, 350), 
                            text_input="OPTIONS", font=get_font(20), base_color="White", hovering_color="Red")
        QUIT_BUTTON = Button(image=pygame.image.load("Python-Tetris-Game-Pygame-main/assets/Quit Rect.png"), pos=(240, 500), 
                            text_input="QUIT", font=get_font(20), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
def over_menu():
    while True:
       
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("GAME OVER!", True, "YELLOW")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 50))
        
        Pest_TEXT = get_font(20).render("Your score is: ", True, "YELLOW")
        Pest_RECT = Pest_TEXT.get_rect(center=(250, 100))
        
        score_text = get_font(20).render(str(game.pest_score), True, "YELLOW")
        score_rect = score_text.get_rect(center=(250, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("Python-Tetris-Game-Pygame-main/assets/Play Rect.png"), pos=(250, 250), 
                            text_input="Try Again!", font=get_font(20), base_color="White", hovering_color="Red")
        QUIT_BUTTON = Button(image=pygame.image.load("Python-Tetris-Game-Pygame-main/assets/Quit Rect.png"), pos=(250, 430), 
                            text_input="Exit", font=get_font(20), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(Pest_TEXT, Pest_RECT)
        SCREEN.blit(score_text, score_rect)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_again()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()