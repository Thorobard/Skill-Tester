import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Define game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TARGET_RADIUS = 20
TARGET_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 36
GAME_FONT = pygame.font.Font(None, FONT_SIZE)
GAME_TIME = 10 # in seconds
TARGET_SPAWN_INTERVAL = 1000 # in milliseconds
MAX_FPS = 60

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()

# Define game state variables
game_running = False
game_score = 0
game_time_remaining = GAME_TIME * 1000
last_target_spawn_time = 0

# Define game functions
def draw_target(x, y):
    """
    Draws a target at the specified (x, y) position.
    """
    pygame.draw.circle(window, TARGET_COLOR, (x, y), TARGET_RADIUS)

def spawn_target():
    """
    Spawns a new target at a random position.
    """
    x = random.randint(TARGET_RADIUS, WINDOW_WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, WINDOW_HEIGHT - TARGET_RADIUS)
    draw_target(x, y)

def start_game():
    """
    Initializes game state and starts the game.
    """
    global game_running, game_score, game_time_remaining, last_target_spawn_time
    game_running = True
    game_score = 0
    game_time_remaining = GAME_TIME * 1000
    last_target_spawn_time = pygame.time.get_ticks()

def end_game():
    """
    Ends the game and displays the final score.
    """
    global game_running
    game_running = False
    final_score_text = GAME_FONT.render(f"Final Score: {game_score}", True, FONT_COLOR)
    final_score_text_rect = final_score_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    window.blit(final_score_text, final_score_text_rect)

target_x = None
target_y = None
# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_running:
            mouse_pos = pygame.mouse.get_pos()
            distance_to_target = ((target_x - mouse_pos[0])**2 + (target_y - mouse_pos[1])**2)**0.5
            if distance_to_target <= TARGET_RADIUS:
                game_score += 1
                spawn_target()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_running:
                start_game()

    # Update game state
    current_time = pygame.time.get_ticks()
    last_time = current_time
    if game_running and current_time - last_target_spawn_time >= TARGET_SPAWN_INTERVAL:
        spawn_target()
        last_target_spawn_time = current_time
    if game_running:
        game_time_remaining = max(0, game_time_remaining - (current_time - last_time))
        if game_time_remaining == 0:
            end_game()
    

    # Draw the game window
    window.fill(BACKGROUND_COLOR)
    if game_running:
        target_x = random.randint(TARGET_RADIUS, WINDOW_WIDTH - TARGET_RADIUS)
        target_y = random.randint(TARGET_RADIUS, WINDOW_HEIGHT - TARGET_RADIUS)
        draw_target(target_x, target_y)
        game_time_text = GAME_FONT.render(f"Time: {game_time_remaining//1000}", True, FONT_COLOR)
        game_score_text = GAME_FONT.render(f"Score: {game_score}", True, FONT_COLOR)
        window.blit(game_time_text, (10, 10))
        window.blit(game_score_text, (WINDOW_WIDTH - game_score_text.get_width() - 10, 10))
         # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the mouse click is within the target
                if math.sqrt((event.pos[0] - target_x)**2 + (event.pos[1] - target_y)**2) < TARGET_RADIUS:
                    game_score += 1

        # Update game state
        if game_running:
            game_time_remaining -= delta_time
            if game_time_remaining <= 0:
                game_running = False

        # Cap the frame rate
        clock.tick(MAX_FPS)

    # Display the final score
    final_score_text = GAME_FONT.render(f"Final Score: {game_score}", True, FONT_COLOR)
    window.blit(final_score_text, ((WINDOW_WIDTH - final_score_text.get_width()) // 2, WINDOW_HEIGHT // 2))
    pygame.display.update()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
              