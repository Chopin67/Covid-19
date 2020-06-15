import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)

box3 = gamebox.from_color(200,400,"black",30,40)
box = gamebox.from_color(camera.x,camera.bottom,"green",800,100)

r = random.randrange(0,800)

walls = [

    [gamebox.from_color(camera.x, camera.bottom, "green", 50, r),
    gamebox.from_color(camera.x,camera.top, "green", 50, 900-r)]]

walls2 = [

    [gamebox.from_color(camera.x+400, camera.bottom, "green", 50, r),
    gamebox.from_color(camera.x+400, camera.top, "green", 50, 900 - r)]

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

    global walls
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
    camera.draw(box)
    if pygame.K_SPACE in keys and box3.timer > 3:
        box3.y -= 80
        box3.timer = 0
    else:
        box3.y += 7


    box3.timer += 1
    #for wall in walls:
        #box3.move_to_stop_overlapping(wall)

    for list in walls:
        global r
        list[0].x -= 5
        list[1].x -= 5
        camera.draw(list[0])
        camera.draw(list[1])
        r = random.randrange(0, 600)

        if list[0].right < camera.left:
            list.remove(list[0])
            list.append(list[0])
            list[0] = gamebox.from_color(camera.x + 400, camera.bottom, "green", 50, r)

            list[0].x = camera.right

        if list[1].right < camera.left:
            list.remove(list[1])
            list.append(gamebox.from_color(camera.x + 400, camera.top, "green", 50, 900 - r))
            list[1].x = camera.right


        if box3.touches(list[1]) or box3.touches(list[0]):
            lost = gamebox.from_text(camera.x,camera.y, "You Lost","Arial",150,"white",bold=True)
            camera.draw(lost)
            scoree = gamebox.from_text(camera.x,camera.y+100, "Score:","Arial",50,"white",bold=True)
            sc = gamebox.from_text(camera.x+100,camera.y+100,str(ticks//30),"Arial",50,"white",bold=True)
            camera.draw(scoree)
            camera.draw(sc)
            gamebox.pause()


    for thing in walls2:

        thing[0].x -= 5
        thing[1].x -= 5

        camera.draw(thing[0])
        camera.draw(thing[1])

        r = random.randrange(0, 600)
        if thing[0].right < camera.left:
            thing.remove(thing[0])


            thing.append(thing[0])
            thing[0] = gamebox.from_color(camera.x + 400, camera.bottom, "green", 50, r)
            thing[0].x = camera.right
        if thing[1].right < camera.left:
            thing.remove(thing[1])
            thing.append(gamebox.from_color(camera.x + 400, camera.top, "green", 50, 900 - r))
            thing[1].x = camera.right
        # if list[1].right < camera.left:
        #     list[1] = gamebox.from_color(camera.x, camera.top, "green", 50, 900 - r)


        if box3.touches(thing[1]) or box3.touches(thing[0]):
            lost = gamebox.from_text(camera.x,camera.y, "You Lost","Arial",150,"white",bold=True)
            camera.draw(lost)
            gamebox.pause()
        if box3.touches(thing[1]) or box3.touches(thing[0]):
            lost = gamebox.from_text(camera.x,camera.y, "You Lost","Arial",150,"white",bold=True)
            camera.draw(lost)
            scoree = gamebox.from_text(camera.x,camera.y+100, "Score:","Arial",50,"white",bold=True)
            sc = gamebox.from_text(camera.x+100,camera.y+100,str(ticks//30),"Arial",50,"white",bold=True)
            camera.draw(scoree)
            camera.draw(sc)
            gamebox.pause()
    if box3.touches(box):
        lost = gamebox.from_text(camera.x, camera.y, "You Lost", "Arial", 150, "white", bold=True)
        camera.draw(lost)
        scoree = gamebox.from_text(camera.x, camera.y + 100, "Score:", "Arial", 50, "white", bold=True)
        sc = gamebox.from_text(camera.x + 100, camera.y + 100, str(ticks // 30), "Arial", 50, "white", bold=True)
        camera.draw(scoree)
        camera.draw(sc)
        gamebox.pause()

    camera.display()
ticks_per_second = 30

gamebox.timer_loop(ticks_per_second,tick)
