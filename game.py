import pygame
pygame.init()
window=pygame.display.set_mode((800, 500))
background=pygame.image.load("background.png")
clock=pygame.time.Clock()
class GameSprite():
    def __init__ (self, x=0, y=0, height=0, width=0, step=0, image_sprite=""):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.step=step
        self.image=pygame.image.load(image_sprite)
        self.image=pygame.transform.scale(self.image,(self.width, self.height))
    def draw(self, x, y, ):
        window.blit(self.image,(self.x, self.y))
    def update(self):
        keys = pygame.key.get_pressed()
        if event.key==pygame.K_w:
            self.y-=self.step
        if event.key==pygame.K_s:
            self.y+=self.step
        if event.key==pygame.K_d:
            self.x+=self.step
        if event.key==pygame.K_a:
            self.y-=self.step
        
player=GameSprite(100, 100, 100, 100,10,"player.png")

game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    window.blit(background, (0, 0))
    player.draw(100, 100)
    clock.tick(40)
    pygame.display.update()
pygame.quit()