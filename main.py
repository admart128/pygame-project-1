import pygame
pygame.init()

blue = (0,0,200)
size = (700,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame-project-1")
clock = pygame.time.Clock()

done = False

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (64,64))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

player = Sprite("/home/adam/repos/pygame-project-1/player.png")

def show_time():
    screen.blit(player.image, (player.rect.x, player.rect.y))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.rect.x -= speed

    if keys[pygame.K_RIGHT]:
        player.rect.x += speed

    if keys[pygame.K_DOWN]:
        player.rect.y += speed

    if keys[pygame.K_UP]:
        player.rect.y -= speed


x = 0
y = 0
speed = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    screen.fill(blue)
    show_time()
    pygame.display.flip()
    clock.tick(60)  # limit the frame rate to 60 fps

pygame.quit()




