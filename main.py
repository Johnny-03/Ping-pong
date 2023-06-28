from pygame import*
back = (200,250,200)
w,h = 600,500
window = display.set_mode((w,h))
window.fill (back)
game,finish = True,False
clock = time.Clock()
fps = 60
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)