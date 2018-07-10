import pygame

pygame.init()

win_height = 500
win_width = 500
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Cubes")

walkRight = [pygame.image.load('right1.png'),
             pygame.image.load('right2.png'),
             pygame.image.load('right3.png'),
             pygame.image.load('right4.png'),
             pygame.image.load('right5.png')]

walkLeft = [pygame.image.load('left1.png'),
            pygame.image.load('left2.png'),
            pygame.image.load('left3.png'),
            pygame.image.load('left4.png'),
            pygame.image.load('left5.png')]

bg = pygame.image.load('back.jpg')
playerStand_Left = pygame.image.load('stand_left.png')
playerStand_Right = pygame.image.load('stand_right.png')
clock = pygame.time.Clock()

x = 50
y = 350
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

left = False
standLeft = False
right = False
animCount = 0


class bullet():
    def __init__(self, x, y, rad, color, facing):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 25:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    elif standLeft:
        win.blit(playerStand_Left, (x, y))
    else:
        win.blit(playerStand_Right, (x, y))

    for bull in bullets:
        bull.draw(win)

    pygame.display.update()


run = True
bullets = []
while run:
    clock.tick(30)
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bul in bullets:
        if bul.x < win_height and bul.x > 0:
            bul.x += bul.vel
        else:
            bullets.pop(bullets.index(bul))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if standLeft == False:
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(bullet(round(x + width // 2),
                                  round(y + height // 2), 5, (0, 255, 0), facing))
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        standLeft = True
    elif keys[pygame.K_RIGHT] and x < win_width - width - 5:
        x += speed
        left = False
        right = True
        standLeft = False
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
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

    drawWindow()
pygame.quit()
