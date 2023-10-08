from textwrap import fill
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

def check_win(box_filled):
    if box_filled[0] == box_filled[1] and box_filled[1] == box_filled[2] and box_filled[0] != 0:
        print("W1")
    elif box_filled[0] == box_filled[3] and box_filled[3] == box_filled[6] and box_filled[0] != 0:
        print("W2")
    elif box_filled[6] == box_filled[7] and box_filled[7] == box_filled[8] and box_filled[6] != 0:
        print("W3")
    elif box_filled[2] == box_filled[5] and box_filled[5] == box_filled[8] and box_filled[2] != 0:
        print("W4")
    elif box_filled[0] == box_filled[4] and box_filled[4] == box_filled[8] and box_filled[0] != 0:
        print("W5")
    elif box_filled[2] == box_filled[4] and box_filled[4] == box_filled[6] and box_filled[2] != 0:
        print("W6")
    elif box_filled[1] == box_filled[4] and box_filled[4] == box_filled[7] and box_filled[1] != 0:
        print("W7")
    elif box_filled[3] == box_filled[4] and box_filled[4] == box_filled[5] and box_filled[3] != 0:
        print("W8")

filled = 0
player = 1
box_filled = [0,0,0,0,0,0,0,0,0]

while True:
    left,middle,right = pygame.mouse.get_pressed()

    if left:
        pos = pygame.mouse.get_pos()
        x,y = pos
    
        filling = 1

        if x <= 266:
            if y <= 200:
                print("1")
                if box_filled[0] != 0:
                    filling = 0
                else:
                    player_draw(player,0,0)
                    box_filled[0] = 1 + player
            elif y <= 400:
                print("2")
                if box_filled[1] != 0:
                    filling = 0
                else:
                    player_draw(player,0,200)
                    box_filled[1] = 1 + player
            else:
                print("3")
                if box_filled[2] != 0:
                    filling = 0
                else:
                    player_draw(player,0,400)
                    box_filled[2] = 1 + player
        elif x <= 532:            
            if y <= 200:
                print("4")
                if box_filled[3] != 0:
                    filling = 0
                else: 
                    player_draw(player,266,0)
                    box_filled[3] = 1 + player
            elif y <= 400:
                print("5")
                if box_filled[4] != 0:
                    filling = 0
                else:
                    player_draw(player,266,200)
                    box_filled[4] = 1 + player
            else:
                print("6")
                if box_filled[5] != 0:
                    filling = 0
                else:
                    player_draw(player,266,400)
                    box_filled[5] = 1 + player
        else:
            if y <= 200:
                print("7")
                if box_filled[6] != 0:
                    filling = 0
                else:
                    player_draw(player,532,0)
                    box_filled[6] = 1 + player
            elif y <= 400:
                print("8")
                if box_filled[7] != 0:
                    filling = 0
                else:
                    player_draw(player,532,200)
                    box_filled[7] = 1 + player
            else:
                print("9")
                if box_filled[8] != 0:
                    filling = 0
                else: 
                    player_draw(player,532,400)
                    box_filled[8] = 1 + player
        if filling == 1:
            player = 1 - player
            filled = filled + 1
            check_win(box_filled)
    if filled == 9:
        print("End")


    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            quit()
    pygame.display.update()
    clock.tick(10)


