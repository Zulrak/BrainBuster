# Source File Name: BrainBuster_Version_0_4
# Author's Name: Jordan Cooper
# Last Modified By: Jordan Cooper
# Date Last Modified: Friday, July 11, 2013
""" 
  Program Description:  Brain Buster is a side scroller game where the user must consume as many brains
                        as possible before he is destroied by the angry villagers. To consume brains the user
                        must simply manuver Doug the Zombie (your avatar) with your mouse coming in contact
                        with the Healthy Brains (pink), avoiding the Poisonous Brains (green) and the angry villagers! 
                        
        Version: 0.4    - added an intorduction screen
                        - added a new background picture for the side scroller
                        - added an end screen
                        - adjusted the x coordinate spawn range so that enemies and Objectives will not be cut off of the screen
"""
import random
import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

#Create the Avatar Named Doug the Zombie
class DougTheZombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("DougTheZombie.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

#Update the Doug Avatar       
    def update(self):
        ''' Get Mouse position, set the y position and a fixed position to the sprite'''
        mousex , mousey = pygame.mouse.get_pos()
        self.rect.center = (125,mousey)
        
        ''' If the Avatar is moving off the screen, set the avatar to the top of the screen.'''
        if mousey < (42): 
            self.rect.center = (125,42)
        if mousey > (438): 
            self.rect.center = (125,438)

#Create the Objective sprit, the Brain           
class Brain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("brain.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5

#Move the brain left 5px Until the brain leaves the player's feild of view
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
#Reset the brain to a randomized position BEHIND the player's feild of view           
    def reset(self):
        self.rect.left = 0
        self.rect.centerx = random.randrange(700, 900)
        self.rect.centery = random.randrange(20, 438)

#Create the first enemy sprite, the poison brain       
class PoisonBrain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("PoisonBrain.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
        
#Move the poison brain left into the player's feild of view    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
#Reset the poison brain's position to a randomized location off of the player's feild of view      
    def reset(self): 
        self.rect.left = 0
        self.rect.centerx = random.randrange(700, 900)
        self.rect.centery = random.randrange(20, 438)

#Create the second enemy, the angry villager                
class Villager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("villager.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 7

#Move the angry villager 7px to the left, to appear as if charging at the zombie    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
  
#Reset the villager's position to a randomized location off of the player's feild of view            
    def reset(self):
        self.rect.left = 0
        self.rect.centerx = random.randrange(700, 900)
        self.rect.centery = random.randrange(40, 438)
        
#Create the background image for the side scroller
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ground.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 5
        self.reset()

#Move the Background Image at a rate of 5px, Reset the image once almost 3/4 of the image has been displayed
#This will make the image seem as if it is never ending       
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -1900:
            self.reset() 

#Reset the Background Image to the left side of the page  
    def reset(self):
        self.rect.left = 0

#Calculate the score for the player and the player's health
class PointCalculator(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.healthBar = 100
        self.brainCount = 0
        self.font = pygame.font.SysFont("None", 50)
 
#Display the Health bar and Brain count as they are changed (See GameScreen's Collisison detection)       
    def update(self):
        self.text = "life: %d, Brains: %d" % (self.healthBar, self.brainCount)
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

#The game's actual play screen           
def GameScreen():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Brain Buster Version 0.4")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    
    #Avatar (100 health) (Takes Damage)
    dougTheZombie = DougTheZombie()
    #Objectives (+1 brain count)
    brain1 = Brain()
    brain2 = Brain()
    brain3 = Brain()
    #Enemy 1 (+10 damage)
    poisonBrain = PoisonBrain()
    #Enemy 2 (+25 damage)
    villager1 = Villager()
    villager2 = Villager()
    villager3 = Villager()
    #Display Player's score and health
    pointCalculator = PointCalculator()
    #Game screen background
    ground = Ground()
    
    #Sprite groups
    friendSprites = pygame.sprite.OrderedUpdates(ground,dougTheZombie, poisonBrain)
    brainSprites = pygame.sprite.Group(brain1,brain2,brain3)
    villagerSprites = pygame.sprite.Group(villager1,villager2,villager3)
    pointSprites = pygame.sprite.Group(pointCalculator)
    
    #Game Loop
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #Collision detection Avatar VS Poison Brain (-10HP)
        if dougTheZombie.rect.colliderect(poisonBrain.rect):
            pointCalculator.healthBar -= 10
            if pointCalculator.healthBar <= 0:
                keepGoing = False
            poisonBrain.reset()
        
        #Collision detection Avatar VS Villager (-25HP)
        vilagerHit = pygame.sprite.spritecollide(dougTheZombie, villagerSprites, False)
        if vilagerHit:
            pointCalculator.healthBar -= 25
            if pointCalculator.healthBar <= 0:
                keepGoing = False
            for theVillager in vilagerHit:
                theVillager.reset()
                
        #Collision detection Avatar VS Brain (+ 1 Brain)
        brainHit = pygame.sprite.spritecollide(dougTheZombie, brainSprites, False)
        if brainHit:
            pointCalculator.brainCount += 1
            for thePBrain in brainHit:
                thePBrain.reset()
           
        #Update and draw friendSprites     
        friendSprites.update()
        friendSprites.draw(screen)
        #Update and draw villagerSprites    
        villagerSprites.update()
        villagerSprites.draw(screen)
        #Update and draw brainSprites      
        brainSprites.update()
        brainSprites.draw(screen)
        #Update and draw pointSprites     
        pointSprites.update()
        pointSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    
    return pointCalculator.brainCount
 
def instructions(brainCount):
    pygame.display.set_caption("Brain Buster!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #Generate the Instructions screen
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Brain Buster.     Last score: %d" % brainCount ,
    "",
    "Instructions: You are the Zombie,",
    "to survive all zombies need brains.",
    "Collect as many brains as you can,",
    "but be careful not to eat those",    
    "poisonous brains or hug those",
    "mean villagers they will KILL YOU!",
    "Move doug with your mouse and",
    "get those yummy brains!",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
         
    pygame.mouse.set_visible(True)
    return donePlaying

def endGame(brainCount):
    pygame.display.set_caption("Brain Buster!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Brain Buster.     Last score: %d" % brainCount ,
    "",
    "",
    "",
    "",
    "                You Have Died!",    
    "",
    "                      Score: %d" % brainCount,
    "",
    "                     REPLAY? ",
    "",
    "",
    "",
    "click to replay, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
         
    pygame.mouse.set_visible(True)
    return donePlaying
   
def main():
    donePlaying = False
    brainCount = 0
    while not donePlaying:
        donePlaying = instructions(brainCount)
        if not donePlaying:
            brainCount = GameScreen()
            donePlaying = endGame(brainCount)
    
if __name__ == "__main__":
    main()
            
