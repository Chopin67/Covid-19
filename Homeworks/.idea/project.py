import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

show_splash = True
ticks = 0
box = gamebox.from_color(400, random.randrange(1, 599), 'orange', 30, 30)
player1 = gamebox.from_color(700, 10, 'red', 30, 30)
player2 = gamebox.from_color(100, 10, 'blue', 30, 30)
title = gamebox.from_text(camera.x, camera.y, 'WELCOME TO REPTILIA', 'Helvetica', 36, 'green')


def splash(keys):
    global show_splash
    camera.clear("black")


    camera.draw(gamebox.from_text(camera.x, camera.y + 50, "Blue player: Use W,A,S,D keys to move", "Arial", 20, "white"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 70, "Red player: Use arrow keys to move", "Arial", 20, "white"))
    camera.draw(gamebox.from_text(camera.x, camera.y + 120, "Press SPACE to continue", "Arial", 30, "white"))

    camera.draw(player1)
    camera.draw(player2)
    camera.draw(title)

    if ticks > 60:
        show_splash = False
    if pygame.K_SPACE in keys:
        show_splash = False
    camera.display()


def tick(keys):
    if show_splash:
        splash(keys)
        Return
    camera.clear('black')
    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
