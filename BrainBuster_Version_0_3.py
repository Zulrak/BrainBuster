# Source File Name: BrainBuster_Version_0_3
# Author's Name: Jordan Cooper
# Last Modified By: Jordan Cooper
# Date Last Modified: Friday, July 10, 2013
""" 
  Program Description:  Brain Buster is a side scroller game where the user must consume as many brains
                        as possible before he is destroied by the angry villagers. To consume brains the user
                        must simply manuver Doug the Zombie (your avatar) with your mouse coming in contact
                        with the Healthy Brains (pink), avoiding the Poisonous Brains (green) and the angry villagers! 
                        
        Version: 0.3    - created a group of brains (coins)
                        - created a group of villagers (enemies)        
                        - created a PointCalculator class that will calculate health and brain count
                        - attached the health and brain count to the brains and enemy mobs             
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

class PointCalculator(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.HealthBar = 100
        self.BrainCount = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "life: %d, Brains: %d" % (self.HealthBar, self.BrainCount)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
            
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Brain Buster Version 0.3")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    
    dougTheZombie = DougTheZombie()
    
    brain1 = Brain()
    brain2 = Brain()
    brain3 = Brain()
    
    ground = Ground()
    
    villager1 = Villager()
    villager2 = Villager()
    villager3 = Villager()
    
    poisonBrain = PoisonBrain()
    
    pointCalculator = PointCalculator()

    friendSprites = pygame.sprite.OrderedUpdates(ground,dougTheZombie, poisonBrain)
    brainSprites = pygame.sprite.Group(brain1,brain2,brain3)
    villagerSprites = pygame.sprite.Group(villager1,villager2,villager3)
    pointSprites = pygame.sprite.Group(pointCalculator)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # Create the collision detection for our avatar,objectives and enemies
        if dougTheZombie.rect.colliderect(poisonBrain.rect):
            pointCalculator.HealthBar -= 10
            if pointCalculator.HealthBar <= 0:
                keepGoing = False
            poisonBrain.reset()
        
        #Collision detection between doug the zombie and the angry villagers.
        vilagerHit = pygame.sprite.spritecollide(dougTheZombie, villagerSprites, False)
        if vilagerHit:
            pointCalculator.HealthBar -= 25
            if pointCalculator.HealthBar <= 0:
                keepGoing = False
            for theVillager in vilagerHit:
                theVillager.reset()
                
        #Collision detection between doug the zombie and the brain object.
        brainHit = pygame.sprite.spritecollide(dougTheZombie, brainSprites, False)
        if brainHit:
            pointCalculator.BrainCount += 1
            for thePBrain in brainHit:
                thePBrain.reset()
           
                
        friendSprites.clear(screen, background)
        friendSprites.update()
        friendSprites.draw(screen)
        
        villagerSprites.update()
        villagerSprites.draw(screen)
        
        brainSprites.update()
        brainSprites.draw(screen)

        pointSprites.update()
        pointSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
