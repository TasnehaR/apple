import pygame
import random
from apple import Apple
from zap import Zap
import time

pygame.init()
# FONTS
pygame.font.init()
my_font = pygame.font.SysFont('ArialBlack', 20)
# SCREEN
pygame.display.set_caption("Shoot the Fruit!")
size = (600, 400)
screen = pygame.display.set_mode(size)
# TEXT
text = my_font.render("Click the fruit to score!", True, (115, 79, 150))
win_message = my_font.render("Game over! You win!", True, (255, 50, 255))
message_x = 300 - win_message.get_width()
message_y = 200 - win_message.get_height()
# POINTS
points = 0
point_display = my_font.render("Points: " + str(points), True, (115, 79, 150))
# TIME
start_time = time.time()
# APPLE OBJECT
a = Apple(50, 50)
z = Zap(700, 800)

run = True
game_over = False
lose = False
last = 0

while run:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False


       # IF MOUSE CLICKS ON APPLE
       if event.type == pygame.MOUSEBUTTONUP:
           mouse_x = event.pos[0]
           mouse_y = event.pos[1]
           mouse_position = (mouse_x, mouse_y)
           if a.rect.collidepoint(mouse_position):
               rand_x = random.randint(10, 500)
               rand_y = random.randint(10, 300)
               a.move(rand_x, rand_y)
               points = points + 1
               point_display = my_font.render("Points: " + str(points), True, (115, 79, 150))
           elif z.rect.collidepoint(mouse_position):
               lose = True
               game_over = True
           else:
               points = points - 1
               point_display = my_font.render("Points: " + str(points), True, (115, 79, 150))

       # IF POINTS = 10
       if points == 10:
           game_over = True

       if points < 0:
           lose = True
           game_over = True

   # ELAPSED TIME
   if game_over == False:
       time_elapsed = time.time() - start_time  # sets timer to 0
       time_elapsed_int = round(time_elapsed, 2)
       time_string = "Elapsed time: " + str(time_elapsed_int) + " s"  # put time into a string
       display_timer = my_font.render(time_string, True, (115, 79, 150))  # render time

       if time_elapsed_int == (last + 1):
           rand_x = random.randint(10, 500)
           rand_y = random.randint(10, 300)
           z = Zap(rand_x, rand_y)
           last = time_elapsed_int

   # DISPLAY EVERYTHING
   screen.fill((220, 208, 255))

   if game_over == False:
       screen.blit(a.image, a.rect)
       display_timer = my_font.render(time_string, True, (115, 79, 150))
       screen.blit(display_timer, (10, 48))
       screen.blit(point_display, (10, 29))
       screen.blit(text, (10, 10))
       screen.blit(z.image, z.rect)

   if game_over == True:
       if lose == False:
           screen.fill((220, 208, 255))
           win_message = my_font.render("Game over! You win! " + time_string, True, (255, 50, 255))
           center = win_message.get_rect(center=(600 / 2, 400 / 2))
           screen.blit(win_message, center)
       else:
           screen.fill((0, 0, 0))
           lose_message = my_font.render("Game Over! You lose!", True, (255, 255, 255))
           center = lose_message.get_rect(center=(600 / 2, 400 / 2))
           screen.blit(lose_message, center)

       # play_again = my_font.render("Press the space bar to play again", True, (255,50,255))
       # screen.blit(play_again, (50,50))

       for event in pygame.event.get():
           if event.type == (pygame.KEYDOWN):
               if  event.key == pygame.K_SPACE:
                   game_over = False
                   points = 0
                   point_display = my_font.render("Points: " + str(points), True, (115, 79, 150))
                   time_elapsed_int = 0
                   time_string = "Elapsed time: " + str(time_elapsed_int) + " s"  # put time into a string
                   display_timer = my_font.render(time_string, True, (115, 79, 150))  # render time

   pygame.display.update()

