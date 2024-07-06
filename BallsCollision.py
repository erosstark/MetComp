import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Balls Collision Simulation')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
NUM_BALLS = 100
RADIUS = 10
SPEED = 5

class Ball:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off the walls
        if self.x - RADIUS < 0 or self.x + RADIUS > WIDTH:
            self.vx = -self.vx
        if self.y - RADIUS < 0 or self.y + RADIUS > HEIGHT:
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), RADIUS)

    def check_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 2 * RADIUS:
            # Elastic collision response
            angle = math.atan2(dy, dx)
            sin_a = math.sin(angle)
            cos_a = math.cos(angle)

            # Rotate velocities to collision frame
            v1 = (self.vx * cos_a + self.vy * sin_a, -self.vx * sin_a + self.vy * cos_a)
            v2 = (other.vx * cos_a + other.vy * sin_a, -other.vx * sin_a + other.vy * cos_a)

            # Exchange velocities in collision frame
            v1, v2 = v2, v1

            # Rotate velocities back to normal frame
            self.vx = v1[0] * cos_a - v1[1] * sin_a
            self.vy = v1[0] * sin_a + v1[1] * cos_a
            other.vx = v2[0] * cos_a - v2[1] * sin_a
            other.vy = v2[0] * sin_a + v2[1] * cos_a

def create_balls(num_balls):
    balls = []
    for _ in range(num_balls):
        x = random.randint(RADIUS, WIDTH - RADIUS)
        y = random.randint(RADIUS, HEIGHT - RADIUS)
        vx = random.uniform(-SPEED, SPEED)
        vy = random.uniform(-SPEED, SPEED)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        balls.append(Ball(x, y, vx, vy, color))
    return balls

def main():
    clock = pygame.time.Clock()
    balls = create_balls(NUM_BALLS)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for ball in balls:
            ball.move()
            ball.draw()

        # Check for collisions
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls[i].check_collision(balls[j])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
