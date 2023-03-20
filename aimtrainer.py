import pygame
import random
import math

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 720

TARGET_COLOR = (255, 0 , 0)
TARGET_RADIUS = 20

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Aim Trainer")
font = pygame.font.SysFont('Arial', 30)

hits = 0
misses = 0
aim_time = 0
aim_speed = 0
round_average_aim_speed = 0
game_state = "wait"
average_aim_speed = 0
aim_speed_list = []

class TextRect:

    def __init__(self, the_text, color, x, y):
        self.text = font.render(the_text , True, color)
        window.blit(self.text, self.text.get_rect(center=(x, y)))
        

class Target:
    
    def __init__(self):
        self.x = random.randint(
            TARGET_RADIUS, 
            WINDOW_WIDTH - TARGET_RADIUS)
        
        self.y = random.randint(
            TARGET_RADIUS, 
            WINDOW_HEIGHT - TARGET_RADIUS - 60)
        
        pygame.draw.circle(
            window, TARGET_COLOR, 
            (self.x, self.y), TARGET_RADIUS) 
        
          
    def draw(self):
        pygame.draw.circle(window, TARGET_COLOR, (self.x, self.y), TARGET_RADIUS)


target_object = Target()
target_object.draw()

while True:

    current_game_time = pygame.time.get_ticks()
    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            target_x, target_y = target_object.x, target_object.y

            if math.sqrt((target_object.x - mouse_x)**2
                          + (target_object.y - mouse_y)**2) <= TARGET_RADIUS:
                
                
                target_object = Target()
                target_object.draw()
          
                if game_state == "running":

                    aim_speed = current_game_time - aim_time             
                    aim_time = current_game_time
                    hits += 1
                    
                    aim_speed_list.append(aim_speed)                    
                    aim_speed_sum = sum(aim_speed_list)

                    average_aim_speed = aim_speed_sum / hits 
                    round_average_aim_speed = round(average_aim_speed)               
                    
            else:
                misses += 1
                if game_state == "running":
                    aim_speed =+ 200
                

            game_state = "running"        
            window.fill("black")

            target_object.draw()

            hit_text = TextRect(
                the_text=f"Hits: {hits}", 
                x=WINDOW_WIDTH/2-75, 
                y=WINDOW_HEIGHT-30, color="white")
            
            miss_text = TextRect(
                the_text=f"Misses: {misses}", 
                x=WINDOW_WIDTH/2+75,          
                y=WINDOW_HEIGHT-30, color="white")
            
            aim_speed_text = TextRect(
                the_text=f"Aim Speed: {aim_speed}", 
                x=WINDOW_WIDTH/2+300, 
                y=WINDOW_HEIGHT-30, color="white")
               
            round_average_aim_speed_text = TextRect(
                the_text=f"Average Aim Speed: {round_average_aim_speed}",
                x=WINDOW_WIDTH/2-350, 
                y=WINDOW_HEIGHT-30, color="white")

    pygame.display.flip()