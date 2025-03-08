import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
AGENT1_COLOR = (0, 128, 255)  # Blue
AGENT2_COLOR = (255, 0, 0)  # Red
TEXT_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame AI Simulation with Two Agents")

# Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)

# Agent class for the simulation
class Agent(pygame.sprite.Sprite):
    def __init__(self, x, y, color, control_scheme):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.speed = 5
        self.control_scheme = control_scheme  # Different control sets

    def update(self, keys):
        """Update the agent's position based on key input."""
        if self.control_scheme == "arrow":  # Arrow key controls
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
                self.rect.x += self.speed
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += self.speed
        elif self.control_scheme == "wasd":  # WASD controls
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_d] and self.rect.right < WINDOW_WIDTH:
                self.rect.x += self.speed
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += self.speed

# Create two agents
agent1 = Agent(100, 100, AGENT1_COLOR, "arrow")  # Controlled by arrow keys
agent2 = Agent(200, 200, AGENT2_COLOR, "wasd")   # Controlled by WASD keys

# Setup sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(agent1)
all_sprites.add(agent2)

# Main loop
running = True
while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Update both agents
    all_sprites.update(keys)

    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)

    # Draw all agents
    all_sprites.draw(screen)

    # Display the frame count as an example text (debug info)
    frame_text = font.render(f"Frame: {pygame.time.get_ticks() // 1000}", True, TEXT_COLOR)
    screen.blit(frame_text, (10, 10))

    # Flip the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()
