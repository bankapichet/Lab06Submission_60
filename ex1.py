import sys 
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r
        self.g = g
        self.b = b

    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    
    def __init__(self, x=0, y=0, w=0, h=0,r=0,g=0,b=0):
        Rectangle.__init__(self, x, y, w, h,r,g,b)
    
    def isMouseOn(self):
        x,y=pg.mouse.get_pos()
        if x>=self.x and x<=self.w+self.x and y>=self.y and y<=self.h+self.y:
            return True
        else:
            return False
            
        
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,255,0,0) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0] == 1: # Check mouse pressed
            btn.r=255
            btn.g=0
            btn.b=255
        else:           
            btn.r=127
            btn.g=127
            btn.b=127
    else:
        btn.r=255
        btn.g=0
        btn.b=0
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False