# Source File Name: BrainBuster_Version_0_1
# Author's Name: Jordan Cooper
# Last Modified By: Jordan Cooper
# Date Last Modified: Friday, July 3, 2013
""" 
  Program Description:  Brain Buster is a side scroller game where the user must consume as many brains
                        as possible before he is destroied by the angry villagers. To consume brains the user
                        must simply manuver Doug the Zombie (your avatar) with your mouse coming in contact
                        with the Healthy Brains (pink), avoiding the Poisonous Brains (green) and the angry villagers! 
                        
        Version: 0.2    - Fixed some issues with images
                        - created an enemy (villager) 
                        - created another enemy (poisonous Brain)
                        - Fixed spawning issue where the enemies and objectives would only spawn on the top
                        - Added Collision detection between the avatar and all objectes
                        - Added collisison detection between the other objects and eachother
                        
"""
import random
import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

class DougTheZombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("DougTheZombie.gif")


        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        ''' Get Mouse position, set the y position and a fixed position to the sprite'''
        mousex , mousey = pygame.mouse.get_pos()
        self.rect.center = (125,mousey)
        
        ''' If the Avatar is moving off the screen, set the avatar to the top of the screen.'''
        if mousey < (42): 
            self.rect.center = (125,42)
        if mousey > (438): 
            self.rect.center = (125,438)
            
class Brain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("brain.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        
        #I changed that so it makes more sense.
        self.rect.left = 0
    #   self.rect.top = 0
        self.rect.centerx = random.randrange(700, 900)
        self.rect.centery = random.randrange(0, 438)
        
class PoisonBrain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("PoisonBrain.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        
        #I changed that so it makes more sense.
        self.rect.left = 0
    #   self.rect.top = 0
        self.rect.centerx = random.randrange(700, 900)
        self.rect.centery = random.randrange(0, 438)
                
class Villager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("villager.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 7
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        
        #I changed that so it makes more sense.
        self.rect.left = 0
    #   self.rect.top = 0
        self.rect.centerx = random.randrange(700, 900)
        self.rect.centery = random.randrange(0, 438)
        
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("test.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -1160:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

            
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Brain Buster Version 0.1")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    
    dougTheZombie = DougTheZombie()
    brain = Brain()
    ground = Ground()
    villager = Villager()
    poisonBrain = PoisonBrain()
    
    allSprites = pygame.sprite.OrderedUpdates(ground,brain,dougTheZombie,poisonBrain,villager)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # Create the collision detection for our avatar,objectives and enemies
        if dougTheZombie.rect.colliderect(brain.rect):
            brain.reset()
            
        if dougTheZombie.rect.colliderect(poisonBrain.rect):
            poisonBrain.reset()
            
        if dougTheZombie.rect.colliderect(villager.rect):
            villager.reset()
        
        # Stop the brain and poisonous brain from coliding together
        if brain.rect.colliderect(poisonBrain.rect):
            poisonBrain.reset()
            
        if brain.rect.colliderect(villager.rect):
            villager.reset()
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
