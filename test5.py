import pygame
import time

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')





clock = pygame.time.Clock()

font = pygame.font.SysFont(None , 25) #25 defines the size of the message

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [300,300])

def gameLoop():

    lead_x = 300
    lead_y = 300

    lead_x_change = 0     #for continuous pressing of the key, it should move
    lead_y_change = 0

    gameExit = False
    gameOver = True

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press c to contine or q to quit", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -10
                        lead_y_change = 0 #to avoid diagonal movement
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = 10
                        lead_y_change = 0
                    elif event.key == pygame.K_UP:
                        lead_y_change = -10
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = 10
                        lead_x_change = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  
                        lead_x_change = 0 #if we release the key, the snake should stop moving

            if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0:
                gameExit = True
            
            lead_x += lead_x_change
            lead_y += lead_y_change

            gameDisplay.fill(white)
            pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
            pygame.display.update()

            clock.tick(10) #frames per second


        message_to_screen("You lose", red)
        pygame.display.update()
        time.sleep(2)
    pygame.quit()
    quit()

gameLoop()
