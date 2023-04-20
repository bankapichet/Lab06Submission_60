import sys
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height\
        self.r = r
        self.g = g
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(51,153,255),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    
    def __init__(self, x=0, y=0, w=0, h=0,r=0,g=0,b=0):
        Rectangle.__init__(self, x, y, w, h,r,g,b)
    
    def isMouseOn(self):
        x,y=pg.mouse.get_pos()
        if x>=self.x and x<=self.w+self.x and y>=self.y and y<=self.h+self.y:
            return True
        else:
            return False
        
            
        
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable..
                self.active = not self.active #False -> True
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
    
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
class InputBoxnum:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable..
                self.active = not self.active #False -> True
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
    
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                    else:
                        pass

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
                
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(400,340,100,50)

COLOR_INACTIVE = pg.Color(0,0,0) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(0,102,0)     # ^^^
FONT = pg.font.Font(None, 32)
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('Firstname', True, (29,67,218)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (win_x //2,80)
text2 = font.render('Lastname', True, (29,67,218)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (win_x //2,180)
text3 = font.render('Age', True, (29,67,218)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (win_x //2,280)
font = pg.font.Font('freesansbold.ttf', 25)
text4 = font.render('Submit', True, (204,0,204)) # (text,is smooth?,letter color,background color)
bank=''
htext = FONT.render('', True, (0,0,0))
input_box1 = InputBox(300, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(300, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBoxnum(300,300,140,32) # สร้าง InputBox3

input_boxes = [input_box1, input_box2,input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

while run:
    screen.fill((255, 255, 205))
    
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    btn.draw(screen)
    screen.blit(text4, (405,355))
    
    if btn.isMouseOn():
    #     if pg.mouse.get_pressed()[0] == 1: # Check mouse pressed
    #         btn.r=255
    #         btn.g=0
    #         btn.b=255
    #     else:           
    #         btn.r=127
    #         btn.g=127
    #         btn.b=127
    # else:
    #     btn.r=255
    #     btn.g=0
    #     btn.b=0
        
        
        if pg.mouse.get_pressed()[0] == 1: # Check mouse pressed
            if input_box1.text == '' and input_box2.text == '' and input_box3.text == '':
                bank='NO'
            if input_box1.text != '' and input_box2.text != '' and input_box3.text != '':
                bank='YES'
            if input_box1.text == ''and input_box2.text != '' and input_box3.text != '':
                bank='sus'
            if input_box1.text == ''and input_box2.text == '' and input_box3.text != '':
                bank='sad'
            if input_box1.text == ''and input_box2.text != '' and input_box3.text == '' :
                bank='sak'
            if input_box1.text != ''and input_box2.text == '' and input_box3.text == '' :
                bank='sap'
            if input_box1.text != ''and input_box2.text == '' and input_box3.text != '' :
                bank='sal'
            if input_box1.text != ''and input_box2.text != '' and input_box3.text == '' :
                bank='sam'
   
        
        if bank== 'NO':
            txt = 'Input your Name and Age!!'
            htext = FONT.render(txt, True, (255,0,0))        
        if bank== 'YES':
            txt = 'Hello ' + str(input_box1.text) + ' ' + str(input_box2.text) + ' ! You are ' + str(input_box3.text) + ' years old.'
            htext = FONT.render(txt, True, (0,0,0))
        if bank== 'sus':
            txt = ' Hello Mr ' +str(input_box2.text) + ' ! You are ' + str(input_box3.text) + ' years old.'
            htext = FONT.render(txt, True, (0,0,0))
        if bank== 'sad':
            txt =  '  You are ' + str(input_box3.text) + ' years old.'
            htext = FONT.render(txt, True, (0,0,0))
        if bank== 'sak':
            txt =  'Hello Mr.' + str(input_box2.text) 
            htext = FONT.render(txt, True, (0,0,0))
        if bank== 'sap':
            txt = 'Hello ' + str(input_box1.text) 
            htext = FONT.render(txt, True, (0,0,0))
        if bank== 'sal':
            txt =  'Hello '+ str(input_box1.text)  +  '  You are ' + str(input_box3.text) + ' years old.'
            htext = FONT.render(txt, True, (0,0,0))
        if bank== 'sam':
            txt = 'Hello ' + str(input_box1.text)+' '+ str(input_box2.text) 
            htext = FONT.render(txt, True, (0,0,0))
           
           
            # txt = 'Hello ' + str(input_box1.text) + ' ' + str(input_box2.text) + ' ! You are ' + str(input_box3.text) + ' years old.'
            # htext = FONT.render(txt, True, (0,0,0)) 
             
    screen.blit(htext, (25,440))
            
        
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()
