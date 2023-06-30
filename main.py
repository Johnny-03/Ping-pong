from pygame import*
back = (200,250,200)
w,h = 600,500
window = display.set_mode((w,h))
window.fill (back)
game,finish = True,False
clock = time.Clock()
fps = 60
class Gamesprite(sprite.Sprite):
    def __init__(self,p_image,x,y,size_x,size_y,p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def update1(self):
        k = key.get_pressed()
        if k [K_UP] and self.rect.y > 5:
            self.rect.y-=self.speed 
        if k [K_DOWN] and self.rect.y < h-80:
            self.rect.y+=self.speed
    def update2(self):
        k = key.get_pressed()
        if k [K_w] and self.rect.y > 5:
            self.rect.y-=self.speed 
        if k [K_s] and self.rect.y < h-80:
            self.rect.y+=self.speed
recit1 = Player('pngwing.com.png',30,200,30,150,4)
recit2 = Player('pngwing.com.png',520,200,30,150,4)
speed_x, speed_y = 3,3 
Ball = Gamesprite('Ball.png',200,200,50,50,4)
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        window.fill (back)
        recit1.update1()
        recit2.update2()
        Ball.rect.x+=speed_x
        Ball.rect.y+=speed_y
        recit1.reset()
        recit2.reset()
        Ball.reset()
    display.update()
    clock.tick(fps)
