import  pygame
pygame.init()

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#PI
pi=3.141592653

#CLOCK
clock = pygame.time.Clock()

#COORDS_AND_OTHER
x = 2
y = 468
width = 30
height = 27
speed = 10
isJump = False
JumpCount = 10
left = False
right = False
animCount = 0
JC = 0

#WALK_ANIM
walk_RIGHT = [pygame.image.load("figure-R1.gif"), pygame.image.load("figure-R2.gif"), pygame.image.load("figure-R3.gif")]
walk_LEFT = [pygame.image.load("figure-L1.gif"), pygame.image.load("figure-L2.gif"), pygame.image.load("figure-L3.gif")]
stand = pygame.image.load("figure-S.gif")



#PLATFORMS
platform_b = pygame.image.load("platform1.gif")
platform_m = pygame.image.load("platform2.gif")
platform_s = pygame.image.load("platform3.gif")

#DOORS
door_c = pygame.image.load("door1.gif")
door_o = pygame.image.load("door2.gif")

#SCREEN
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY OWN GAME(NO)")

#SPRITES


#DRAWING_FUNCTION
def draw():
    global animCount
    screen.fill(WHITE)

    if animCount + 1 >= 15:
        animCount = 0

    if left:
        screen.blit(walk_LEFT[animCount // 5], (x, y))
        animCount += 1
    elif right:
        screen.blit(walk_RIGHT[animCount // 5], (x, y))
        animCount += 1
    else:
        screen.blit(stand, (x, y))


    #pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
    #pygame.display.update()


def draw_Platforms():
    screen.blit(platform_s, (200, 200))

    screen.blit(platform_b, (300, 400))
    #pygame.display.update()

def draw_Door():
    screen.blit(door_c, (20, 20))
    #pygame.display.update()


def draw_Text():
    # Выбрать шрифт для использования.
    # Стандартный шрифт, размером в 25.
    font = pygame.font.Font(None, 20)

    # Воспроизвести текст. "True" значит,
    # что текст будет сглаженным (anti-aliased).
    # Чёрный - цвет. Переменную BLACK мы задали ранее,
    # списком [0,0,0]
    # Заметьте: эта строка создаёт картинку с буквами,
    # но пока не выводит её на экран.
    text = font.render(str(JC), True, BLACK)

    # Вывести сделанную картинку на экран в точке (250, 250)
    screen.blit(text, (478, 1))
    #pygame.display.update()

def draw_mouse():
    pygame.mouse.set_visible(0)
    pos = pygame.mouse.get_pos()
    x1 = pos[0]
    y1 = pos[1]

    # Рисование
    screen.blit(stand, (x1, y1))
    #pygame.display.update()

looper = True
while looper:
    clock.tick(30)

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looper = False

    #KEYS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 2:
        x -= speed
        left = True
        right = False
    if keys[pygame.K_RIGHT] and x < 467:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        #if keys[pygame.K_UP] and y > 2:
        #    y -= speed
        #if keys[pygame.K_DOWN] and y < 468:
        #    y += speed
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            isJump = True
            JC += 1
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) // 2
            else:
                y -= (JumpCount** 2) // 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
    if keys[pygame.K_ESCAPE]:
        looper = False


    draw()
    draw_Door()
    draw_Text()
    draw_Platforms()
    draw_mouse()
    pygame.display.update()
pygame.quit()
