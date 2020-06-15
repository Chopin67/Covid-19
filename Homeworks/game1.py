import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)

box3 = gamebox.from_color(400,200,"black",50,60)
r = random.randrange(0,800)
walls = [

    gamebox.from_color(camera.x, camera.bottom, "green", 50, r),
    gamebox.from_color(camera.x,camera.top, "green", 50, 900-r),
    gamebox.from_color(camera.x+400, camera.bottom, "green", 50, r),
    gamebox.from_color(camera.x+400, camera.top, "green", 50, 900 - r),

]

show_splash = True
score = 0
box3.timer = 0
ticks = 0


def splash(keys):
    global show_splash
    camera.clear("blue")
    camera.draw(gamebox.from_text(camera.x,camera.y,"FlappyBird-like game by azh5kn", "Arial",30,"black"))
    camera.draw(gamebox.from_text(camera.x,camera.y+50,"(press space to continue)", "Arial",20,"black"))

    camera.display()

    if ticks > 60:
        show_splash = False
    if pygame.K_SPACE in keys:
        show_splash = False
    camera.display()


def tick(keys):
    global ticks
    global r
    ticks += 1

    if show_splash:
        splash(keys)
        return

    camera.clear('cyan')

    time = gamebox.from_text(0,0,str(ticks//30), "Arial", 40, "red")
    time.top = camera.top
    time.right = camera.right-400
    camera.draw(time)

    camera.draw(box3)
    if pygame.K_UP in keys and box3.timer > 3:
        box3.y -= 80
        box3.timer = 0
    else:
        box3.y += 7


    box3.timer += 1
    for wall in walls:
        box3.move_to_stop_overlapping(wall)

    for wall in walls:
        wall.x -= 5
        camera.draw(wall)
        if wall.right < camera.left:
            wall.x = camera.right
            r = random.randrange(0, 800)

            #if box3.touches(wall):
        #    lost = gamebox.from_text(camera.x,camera.y, "You Lost","Arial",150,"white",bold=True)
        #   camera.draw(lost)
        #    gamebox.pause()

    camera.display()
ticks_per_second = 30

gamebox.timer_loop(ticks_per_second,tick)
 