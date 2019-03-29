import sys, pygame
pygame.init()
# https://www.pygame.org/docs/tut/PygameIntro.html
size = width, height = 640, 480
speed = [2, 3]
black = 0, 0, 0
white = 255, 255, 255

# create a graphical window
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ball = pygame.transform.scale(ball,(20,20))
ballrect = ball.get_rect()

paddle = pygame.Surface((7,50))
paddle.fill(white)
paddle_rect = paddle.get_rect()
paddle_rect = paddle_rect.move([50,20])

is_downkey_held = False
is_upkey_held = False

y = 5
# infinite loop
while True:

    if is_downkey_held:
        lower_bound = paddle_rect.bottom + y
        if lower_bound > height:
            paddle_rect = paddle_rect.move([0, height - paddle_rect.bottom])
        else:
            paddle_rect = paddle_rect.move([0,y])

    if is_upkey_held:
        top_bound = paddle_rect.top - y
        if top_bound < 0:
            paddle_rect = paddle_rect.move([0, paddle_rect.top * -1]) 
        else:
            paddle_rect = paddle_rect.move([0, -y])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                is_downkey_held = True
            if event.key == pygame.K_UP:
                is_upkey_held = True
            if event.key == pygame.K_EQUALS:
                if speed[0] <= 0:
                    speed[0] = speed[0] - 1
                if speed[0] > 0:
                    speed[0] = speed[0] + 1
                if speed[1] <= 0:
                    speed[1] = speed[1] - 1
                if speed [1] > 0:
                    speed [1] = speed[1] + 1
            if event.key == pygame.K_MINUS:
                if speed[0] < 0:
                    speed[0] = speed[0] + 1
                if speed[0] > 0:
                    speed[0] = speed[0] - 1
                if speed[1] < 0:
                    speed[1] = speed[1] + 1
                if speed[1] > 0:
                    speed[1] = speed[1] - 1
    
        
        if event.type == pygame.KEYUP:
            is_downkey_held = False
            is_upkey_held = False


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    if ballrect.colliderect(paddle_rect):
        speed[0] = -speed[0]

    screen.fill(black)

    # this draws the ball onto the screen.  without it, the screen would be all black
    screen.blit(ball, ballrect)
    screen.blit(paddle, paddle_rect)

    # now display the new things we've drawn
    pygame.display.flip()