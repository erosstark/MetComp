import pygame
import random
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Balls Collision Simulation')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
NUM_BALLS = 10
RADIUS = 20
SPEED = 5
DEPTH = 500

class Ball:
    def __init__(self, x, y, z, vx, vy, vz, color):
        self.position = np.array([x, y, z], dtype='float64')
        self.velocity = np.array([vx, vy, vz], dtype='float64')
        self.color = color

    def move(self):
        self.position += self.velocity

        # Bounce off the walls
        if self.position[0] - RADIUS < 0 or self.position[0] + RADIUS > WIDTH:
            self.velocity[0] = -self.velocity[0]
        if self.position[1] - RADIUS < 0 or self.position[1] + RADIUS > HEIGHT:
            self.velocity[1] = -self.velocity[1]
        if self.position[2] - RADIUS < -DEPTH or self.position[2] + RADIUS > DEPTH:
            self.velocity[2] = -self.velocity[2]

    def draw(self):
        # Simple perspective projection
        f = WIDTH / (WIDTH + self.position[2])
        x_2d = int(self.position[0] * f)
        y_2d = int(self.position[1] * f)
        pygame.draw.circle(screen, self.color, (x_2d, y_2d), int(RADIUS * f))

    def check_collision(self, other):
        delta_pos = other.position - self.position
        distance = np.linalg.norm(delta_pos)

        if distance < 2 * RADIUS:
            # Elastic collision response
            norm_delta_pos = delta_pos / distance
            relative_velocity = self.velocity - other.velocity
            velocity_along_normal = np.dot(relative_velocity, norm_delta_pos)

            if velocity_along_normal > 0:
                return

            restitution = 1  # Elastic collision

            impulse_magnitude = (-(1 + restitution) * velocity_along_normal) / 2
            impulse = impulse_magnitude * norm_delta_pos

            self.velocity += impulse
            other.velocity -= impulse

def create_balls(num_balls):
    balls = []
    for _ in range(num_balls):
        x = random.randint(RADIUS, WIDTH - RADIUS)
        y = random.randint(RADIUS, HEIGHT - RADIUS)
        z = random.randint(-DEPTH + RADIUS, DEPTH - RADIUS)
        vx = random.uniform(-SPEED, SPEED)
        vy = random.uniform(-SPEED, SPEED)
        vz = random.uniform(-SPEED, SPEED)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        balls.append(Ball(x, y, z, vx, vy, vz, color))
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
