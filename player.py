from circleshape import *
from constants import *
from shot import Shot


class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(screen,color='white',points=self.triangle(),width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
    
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if not (self.timer > 0):
            player_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            player_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            player_shot.position += player_shot.velocity * dt
            self.timer = PLAYER_SHOOT_COOLDOWN
            # starting_vector = pygame.Vector2(0, 1)
            # shot_vector = starting_vector.rotate(self.rotation) * PLAYER_SHOOT_SPEED
            #print("Firing shot!")


