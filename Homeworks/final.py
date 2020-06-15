import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)

show_splash = True
ticks = 0
scorep1 = 0
scorep2 = 0
background = gamebox.from_color(camera.x,camera.y,'black',800,600)

p1 = gamebox.from_color(200,75,'blue',30,29)
p2 = gamebox.from_color(600,75,'orange',30,29)
item = gamebox.from_color(400,random.randrange(1,599),'brown',30,30)
size_variablep1 = 1
size_variablep2 = 1

lives = 3
health = 3
logo = gamebox.from_image(camera.x,camera.y-175,"http://simplyknowledge.com/uploads/page/headimg_url/115/Logo.png")
leaves = gamebox.from_image(camera.x+25,camera.y+225,"https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_960,f_auto/A-dreamstime_xxl_3686826_g50klv.png")

def splash(keys):
   global show_splash
   global logo
   camera.clear("light green")
   camera.draw(gamebox.from_text(camera.x,camera.y-75,"Use keys WASD and the Arrow Keys to control each reptile character.", "Arial",20,"black"))
   camera.draw(gamebox.from_text(camera.x,camera.y-100,"The person to get the highest time before running out of life wins.", "Arial",20,"black"))
   camera.draw(gamebox.from_text(camera.x,camera.y-125,"Alexandra Hickman (azh5kn) and Zach Forstot (zf6pd)", "Arial",20,"black"))

   camera.draw(logo)
   camera.draw(leaves)


   if ticks > 60:
     show_splash = False
   if pygame.K_SPACE in keys:
     show_splash = False
   camera.display()

def tick(keys):
   global scorep1
   global p1
   global size_variablep1
   global p2
   global scorep2
   global size_variablep2
   global lives
   global health
   p1score = gamebox.from_text(200, 30, 'Blue player\'s score is: ' + str(scorep1), 'Arial', 18, 'white')
   p2score = gamebox.from_text(600, 30, 'Orange player\'s score is: ' + str(scorep2), 'Arial', 18, 'white')
   if show_splash:
      splash(keys)
      # camera.draw(logo)
      return
   camera.draw(background)
   camera.draw(p1)
   camera.draw(p2)
   camera.draw(item)

   camera.display()
   if pygame.K_w in keys and (pygame.K_a and pygame.K_d and pygame.K_s not in keys) and p1.speedy == 0:
      p1.speedy = -10
      p1.speedx = 0
      if p1.width >= p1.height:
          p1.size = p1.height, p1.width
   if pygame.K_s in keys and (pygame.K_d and pygame.K_a and pygame.K_w not in keys) and p1.speedy == 0:
      p1.speedy = 10
      p1.speedx = 0
      if p1.width >= p1.height:
          p1.size = p1.height, p1.width
   if pygame.K_a in keys and (pygame.K_s and pygame.K_w and pygame.K_d not in keys) and p1.speedx == 0:
      p1.speedx = -10
      p1.speedy = 0
      if p1.height >= p1.width:
          p1.size = p1.height, p1.width
   if pygame.K_d in keys and (pygame.K_w and pygame.K_s and pygame.K_a not in keys) and p1.speedx == 0:
      p1.speedx = 10
      p1.speedy = 0
      if p1.height >= p1.width:
          p1.size = p1.height, p1.width
   p1.move_speed()


   if pygame.K_UP in keys and (pygame.K_LEFT and pygame.K_RIGHT and pygame.K_DOWN not in keys) and p2.speedy == 0:
      p2.speedy = -10
      p2.speedx = 0
      if p2.width >= p2.height:
          p2.size = p2.height, p2.width
   if pygame.K_DOWN in keys and (pygame.K_LEFT and pygame.K_UP and pygame.K_RIGHT not in keys) and p2.speedy == 0:
      p2.speedy = 10
      p2.speedx = 0
      if p2.width >= p2.height:
          p2.size = p2.height, p2.width
   if pygame.K_LEFT in keys and (pygame.K_DOWN and pygame.K_UP and pygame.K_RIGHT not in keys) and p2.speedx == 0:
      p2.speedx = -10
      p2.speedy = 0
      if p2.height >= p2.width:
          p2.size = p2.height, p2.width
   if pygame.K_RIGHT in keys and (pygame.K_UP and pygame.K_LEFT and pygame.K_DOWN not in keys) and p2.speedx == 0:
      p2.speedx = 10
      p2.speedy = 0
      if p2.height >= p2.width:
          p2.size = p2.height, p2.width
   p2.move_speed()


   if p1.touches(item,-20,-20):
      scorep1 +=1
      size_variablep1 +=1
      print(size_variablep1)
      item.x = random.randrange(10,790)
      item.y = random.randrange(10,590)
      if p1.width > p1.height:
          p1.size = 30 * size_variablep1, 30
      if p1.height > p1.width:
          p1.size = 30, 30 * size_variablep1

   if p1.x < 1 or p1.x > 799:
       p1 = gamebox.from_color(200, 10, 'blue', 30, 29)
       p2 = gamebox.from_color(600, 10, 'orange', 30, 29)
       health -= 1

   if p1.y < 1 or p1.y > 600:
       p1 = gamebox.from_color(200, 10, 'blue', 30, 29)
       p2 = gamebox.from_color(600, 10, 'orange', 30, 29)
       health -= 1

   if p2.touches(item, -20, -20):
       scorep2 += 1
       size_variablep2 += 1
       item.x = random.randrange(10, 790)
       item.y = random.randrange(10, 590)
       if p2.width > p2.height:
           p2.size = 30 * size_variablep2, 30
       if p2.height > p2.width:
           p2.size = 30, 30 * size_variablep2

   if p2.x < 1 or p2.x > 799:
       p1 = gamebox.from_color(200, 10, 'blue', 30, 29)
       p2 = gamebox.from_color(600, 10, 'orange', 30, 29)
       lives -= 1
   if p2.y < 1 or p2.y > 600:
       p1 = gamebox.from_color(200, 10, 'blue', 30, 29)
       p2 = gamebox.from_color(600, 10, 'orange', 30, 29)
       health -= 1

   if p1.touches(p2) or p2.touches(p1):
       health -= 1
       p1 = gamebox.from_color(200, 10, 'blue', 30, 29)
       p2 = gamebox.from_color(600, 10, 'orange', 30, 29)

   if health < 1:
       camera.draw(p2score)
       camera.draw(p1score)
       gamebox.pause()

   # print(lives)



   camera.display()
ticks_per_second = 30

gamebox.timer_loop(ticks_per_second,tick)
