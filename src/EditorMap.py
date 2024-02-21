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
            self.screen.blit(self.paintset_surf, (self.rect_x*8 +10,self.rect_y*8+10 ))
            self.screen.blit(self.controlset_surf,(0,(self.rect_y*15)))
            pygame.display.flip()
        
        pygame.quit()
    
    def splitScreen(self):
        '''
        Este self valdra a futuro para poder hacer la ventana moduar
        
        self.height = self.window.get_height()
        '''
        
        self.tileset_surf = pygame.Surface(((self.rect_x * 8), (self.rect_y*14)))
        self.tileset_surf.fill((255,255,255))
        
        self.paintset_surf = pygame.Surface(((self.rect_x*8),self.rect_y*8 ))
        self.paintset_surf.fill((255,255,255)) 
        
        self.controlset_surf = pygame.Surface(((self.rect_x*3),self.rect_y*2))
        self.controlset_surf.fill((255,255,0))
        
 
e = EditorMap()         