import pygame

pygame.init()

win_height = 500
win_width = 500
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Cubes")

x = 50
y = 435
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < win_width - width - 5:
        x += speed
    if not isJump:
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < win_height - height - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
