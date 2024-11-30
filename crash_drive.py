import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
FPS = 120


# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crash Drive")

# Set up the clock
clock = pygame.time.Clock()

# Set up the car
car_x = WIDTH / 2
car_y = HEIGHT - CAR_HEIGHT - 20
car_speed = 5

# Set up the obstacles
obstacles = []
obstacle_timer = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Add obstacles
    obstacle_timer += 1
    if obstacle_timer > 120:
        obstacle_timer = 0
        obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
        obstacle_y = -OBSTACLE_HEIGHT
        obstacles.append((obstacle_x, obstacle_y))

    # Move obstacles
    for i, (obstacle_x, obstacle_y) in enumerate(obstacles):
        obstacle_y += 5
        obstacles[i] = (obstacle_x, obstacle_y)
        if obstacle_y > HEIGHT:
            obstacles.remove((obstacle_x, obstacle_y))

    # Check for collisions
    for obstacle_x, obstacle_y in obstacles:.3
    
        if (car_x < obstacle_x + OBSTACLE_WIDTH and
            car_x + CAR_WIDTH > obstacle_x and
            car_y < obstacle_y + OBSTACLE_HEIGHT and
            car_y + CAR_HEIGHT > obstacle_y):
            print("Crash!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (car_x, car_y, CAR_WIDTH, CAR_HEIGHT))
    for obstacle_x, obstacle_y in obstacles:
        pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)