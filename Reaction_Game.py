import pygame, time, random
# import required modules

pygame.init()
#initalise pygame

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Reaction Game")

# initalise the screen 

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# assing colour values

Tsoon = False
run = False

# assing bools for checking if the game is over and "won"


def Win():
    if random.randint(1,100) == 55:
        win = True
    else:
        win = False

    return win
# function to determine if the square will turn green

startTime = 0
font = pygame.font.Font(None, 34)

clock = pygame.time.Clock()
screen.fill(black)
pygame.draw.rect(screen, red, (150, 150, 200, 200))

while not run:
    win = Win()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            run = True
            endTime = int(round(time.time() * 1000))
            finishTime = (endTime - startTime)
            
            if not Tsoon:
                soon = font.render("Too soon", 1, white)
                screen.blit(soon, (200, 375))
                pygame.display.flip()
                time.sleep(5)

    if win:       
        startTime = pygame.time.get_ticks()
        pygame.draw.rect(screen, green, (150, 150, 200, 200))
        startTime = int(round(time.time() * 1000))
        Tsoon = True
        
    pygame.display.flip()
    
    clock.tick(20)


if Tsoon:
    score = font.render(str(finishTime), 1, white)
    screen.blit(score, (225, 375))
    pygame.display.flip()
    time.sleep(5)


pygame.quit()
