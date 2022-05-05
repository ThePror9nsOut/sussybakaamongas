import pygame, random, mod

pygame.init()
cap = [1300, 750]; win = pygame.display.set_mode(cap)
run = True
pygame.display.set_caption("")

clock = pygame.time.Clock()
iscl = False
money = 0
acs = 0
pos = [800,350]
lines = []
cam = [0,0]
v = 3
while run:
    c=(random.randint(150,255),random.randint(150,255),random.randint(150,255))
    iscl = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            iscl = True
        else:
            iscl = False
    keys = pygame.key.get_pressed()
    win.fill((0, 0, 0))

    dd = pos[1]+random.randint(-int(v)*4,int(v)*4)
    if(dd>0and dd<750):
        post = (pos[0]+int(v),dd)
    lines.append([pos,post])
    pos = post
    cam[0] = pos[0] - 800
    v+=0.005
    pygame.draw.circle(win,c,(pos[0]-cam[0],pos[1]-cam[1]),5)
    for index,i in enumerate(lines):
        if(i[0][0]-cam[0]<0):
            lines.pop(index)
        else:
            pygame.draw.line(win,c,(i[0][0]-cam[0],i[0][1]),(i[1][0]-cam[0],i[1][1]),5)
    mod.text(win,pygame.font.SysFont("arial black",30),str(money) + "  " + str(acs),(50,50),c)

    if(keys[pygame.K_UP]):
        if(money>750-pos[1]):
            acs += 1
            money -= 750-pos[1]
    if(keys[pygame.K_DOWN]):
        if(acs>0):
            acs -= 1
            money += 750-pos[1]

    money += 1

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
