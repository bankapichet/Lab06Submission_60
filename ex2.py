import sys 
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
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
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
bank=''
while(run):
    screen.fill((153, 255, 255))
    if bank=='D':
        btn.x+=0.1
    if bank=='A':
        btn.x-=0.1
    if bank=='W':
        btn.y-=0.1
    if bank=='S':
        btn.y+=0.1
    if bank=='U':
        pass
    
    btn.draw(screen)
    
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYUP:
            bank= 'U'

        elif event.type == pg.KEYDOWN and  event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            bank='D'
        elif event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดและเป็นปุ่ม A
            bank='A'
        elif event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดและเป็นปุ่ม s
            bank='S'
        elif event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดและเป็นปุ่ม W
            bank='W'