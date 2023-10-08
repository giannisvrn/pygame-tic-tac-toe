import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen_color = (0,0,0)

screen.fill(screen_color)
clock = pygame.time.Clock()
# kathetes
pygame.draw.line(screen,(255,255,255),(266,0),(266,600),15)
pygame.draw.line(screen,(255,255,255),(532,0),(532,600),15)

# orizonties 
pygame.draw.line(screen,(255,255,255),(0,200),(800,200),15)
pygame.draw.line(screen,(255,255,255),(0,400),(800,400),15)

def draw_x(x,y):
    pygame.draw.line(screen,(255,255,255),(10+x,10+y),(250+x,175+y),15)
    pygame.draw.line(screen,(255,255,255),(250+x,10+y),(10+x,175+y),15)

def draw_o(x,y):
    pygame.draw.circle(screen,(255,255,255),(130+x,95+y),90,15)

def player_draw(player,x,y):
    if player == 1:
        draw_x(x,y)
    else:
        draw_o(x,y)

filled = 0
player = 1
while True:
    left,middle,right = pygame.mouse.get_pressed()

    if left:
        pos = pygame.mouse.get_pos()
        x,y = pos
        if x <= 266:
            if y <= 200:
                print("1")
                player_draw(player,0,0)
            elif y <= 400:
                print("2")
                player_draw(player,0,200)
            else:
                player_draw(player,0,400)
                print("3")
        elif x <= 532:            
            if y <= 200:
                print("4")
                player_draw(player,266,0)
            elif y <= 400:
                print("5")
                player_draw(player,266,200)
            else:
                print("6")
                player_draw(player,266,400)
        else:
            if y <= 200:
                print("7")
                player_draw(player,532,0)
            elif y <= 400:
                print("8")
                player_draw(player,532,200)
            else:
                player_draw(player,532,400)
                print("9")
        player = 1 - player
        filled = filled + 1
    if filled == 9:
        print("End")


    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(10)


