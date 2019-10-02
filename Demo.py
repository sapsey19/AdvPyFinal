import pygame

pygame.init()

screenWidth = 500
screenHeight = 500

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Demo')

#player attributes
playerX = 50
playerY = 50
width = 40
height = 60
speed = 3
xvel = 0
yvel = 0

run = True
while run:
    pygame.time.delay(20)  

    #list of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #list of keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    #checks what key is pressed, and checkes for out of bounds
    if keys[pygame.K_LEFT] and playerX > xvel:
        xvel = -1       
    if keys[pygame.K_RIGHT] and playerX < screenWidth - width - xvel:
        xvel = 1            
    if keys [pygame.K_UP] and playerY > yvel:
        yvel = -1        
    if keys [pygame.K_DOWN] and playerY < screenHeight - height - yvel:
        yvel = 1       

    #updates player x and y positions
    playerX += xvel * speed
    playerY += yvel * speed

    #refills the window
    window.fill((0, 0, 0))

    #draws rectangle to the screen
    pygame.draw.rect(window, (255, 0, 0), (playerX, playerY, width, height))
    pygame.display.update()
    xvel = 0
    yvel = 0

pygame.quit()