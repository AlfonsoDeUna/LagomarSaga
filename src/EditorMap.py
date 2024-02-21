import pygame
from pygame.locals import RESIZABLE

class EditorMap:
    
    def __init__(self):
        self.rect_x = 32
        self.rect_y = 32
        self.initializationScreenEditor()

    def initializationScreenEditor(self):
        
        pygame.init()
        self.window = pygame.display.set_mode((800, 600), RESIZABLE)
        pygame.display.set_caption('Map Editor - v0.0.1')
        self.screen = pygame.display.get_surface()
        self.splitScreen()
        self.runningScreen()
       
        
    def runningScreen(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False
                     
            self.window.fill("black")
            self.screen.blit(self.tileset_surf, (0, 0))
            self.screen.blit(self.paintset_surf, (self.rect_x*10 +10,self.rect_y*0 ))
            pygame.display.flip()
        
        pygame.quit()
        
    def splitScreen(self):
        
        self.tileset_surf = pygame.Surface(((self.rect_x*8),self.rect_y*8 ))
        self.tileset_surf.fill((255,255,255))
        
        
        
        self.paintset_surf = pygame.Surface(((self.rect_x*15),self.rect_y*30 ))
        self.paintset_surf.fill((255,255,255)) 
        
 
e = EditorMap()         